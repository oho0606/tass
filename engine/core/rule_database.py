from __future__ import annotations

import json
import re
import sqlite3
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from engine.core.taxonomy import (
    CATEGORY_NAMES,
    CategoryCode,
    parse_category_from_rule_id,
    parse_rule_type,
    to_canonical_id,
)

ROOT = Path(__file__).resolve().parents[2]
DB_DIR = ROOT / "rule_database"
DB_PATH = DB_DIR / "tass_rules.db"
SCHEMA_PATH = DB_DIR / "schema.sql"
REGISTRY_PATH = ROOT / "rules" / "registry.yaml"
CATALOG_DIR = ROOT / "rules" / "catalog"


def _utc_now() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _subcategory_code(category_code: str, name: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", name.strip()).strip("_").upper()
    return f"{category_code}_{slug}"[:48]


@dataclass
class RuleRecord:
    rule_id: str
    rule_name: str
    category_code: str
    subcategory_code: str
    subcategory_name: str
    current_version: str
    status: str
    priority: str
    weight: float
    description: str
    author: str
    rule_type: str
    spec_path: str
    implementation_path: str
    parameters: list[dict[str, Any]] = field(default_factory=list)
    inputs: list[dict[str, Any]] = field(default_factory=list)
    outputs: list[dict[str, Any]] = field(default_factory=list)
    dependencies: list[dict[str, Any]] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    lifecycle_stage: str = "Draft"
    folder_path: str = ""


class RuleDatabase:
    """TASS-013 Rule Database — single source of truth."""

    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path or DB_PATH
        self._conn: sqlite3.Connection | None = None
        self._ensure_db()

    def _connect(self) -> sqlite3.Connection:
        if self._conn is None:
            self._conn = sqlite3.connect(self.db_path, timeout=30)
            self._conn.row_factory = sqlite3.Row
            self._conn.execute("PRAGMA foreign_keys = ON")
            self._conn.execute("PRAGMA journal_mode = WAL")
        return self._conn

    def close(self) -> None:
        if self._conn:
            self._conn.close()
            self._conn = None

    def _ensure_db(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.db_path.exists():
            self._init_schema()
            self.seed_from_registry()
        else:
            row = self._connect().execute("SELECT COUNT(*) AS c FROM rules").fetchone()
            if row and row["c"] == 0:
                self.seed_from_registry()

    def _init_schema(self) -> None:
        conn = self._connect()
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        conn.commit()

    def seed_from_registry(self, registry_path: Path | None = None) -> None:
        path = registry_path or REGISTRY_PATH
        if not path.exists():
            return
        with path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

        conn = self._connect()
        now = _utc_now()
        order = 0
        for code, meta in (data.get("categories") or {}).items():
            order += 10
            conn.execute(
                """INSERT OR REPLACE INTO categories
           (category_code, category_name, description, display_order, enabled, created_at, updated_at)
           VALUES (?, ?, ?, ?, 1, ?, ?)""",
                (code, meta["name"], f"{meta['name']} rules", order, now, now),
            )
            for i, sub_name in enumerate(meta.get("subcategories") or []):
                sc = _subcategory_code(code, sub_name)
                conn.execute(
                    """INSERT OR REPLACE INTO subcategories
             (subcategory_code, category_code, subcategory_name, description, display_order, enabled)
             VALUES (?, ?, ?, ?, ?, 1)""",
                    (sc, code, sub_name, sub_name, i + 1),
                )

        for rule_id, meta in (data.get("rules") or {}).items():
            self._upsert_rule_from_meta(conn, rule_id, meta, now)

        self._seed_from_catalogs(conn, now)

        for alias, canonical in (data.get("legacy_aliases") or {}).items():
            cid = to_canonical_id(canonical)
            conn.execute(
                "INSERT OR REPLACE INTO rule_aliases (alias_id, rule_id, alias) VALUES (?, ?, ?)",
                (str(uuid.uuid4()), cid, alias),
            )
        conn.commit()
        self._sync_rule_folders()

    def _seed_from_catalogs(self, conn: sqlite3.Connection, now: str) -> None:
        """Load frozen category catalogs (TASS-014+). Registry entries take precedence."""
        if not CATALOG_DIR.exists():
            return
        for path in sorted(CATALOG_DIR.glob("*_v*.yaml")):
            self._seed_single_catalog(conn, now, path)

    def _seed_single_catalog(self, conn: sqlite3.Connection, now: str, path: Path) -> None:
        with path.open(encoding="utf-8") as f:
            catalog = yaml.safe_load(f) or {}
        if catalog.get("catalog_type") == "composite":
            self._seed_composite_catalog(conn, now, path, catalog)
            return
        cat_code = catalog.get("category_code")
        if not cat_code:
            return
        catalog_version = catalog.get("catalog_version", "1.0")
        doc_ref = path.stem.replace("_", " ").upper()
        for sub in catalog.get("subcategories") or []:
            sub_name = sub["name"]
            sc = _subcategory_code(cat_code, sub_name)
            conn.execute(
                """INSERT OR REPLACE INTO subcategories
           (subcategory_code, category_code, subcategory_name, description, display_order, enabled)
           VALUES (?, ?, ?, ?, ?, 1)""",
                (sc, cat_code, sub_name, sub_name, 1),
            )
            for rule in sub.get("rules") or []:
                rid = to_canonical_id(rule["id"])
                existing = conn.execute(
                    "SELECT rule_id FROM rules WHERE rule_id = ?", (rid,)
                ).fetchone()
                if existing:
                    continue
                conn.execute(
                    """INSERT INTO rules
             (rule_id, rule_name, category_code, subcategory_code, current_version, status,
              priority, weight, description, author, rule_type, spec_path, implementation_path,
              created_at, updated_at)
             VALUES (?, ?, ?, ?, '1.0.0', 'Frozen', 'Medium', 1.0, ?, 'TASS Project', 'atomic',
                     '', '', ?, ?)""",
                    (rid, rule["name"], cat_code, sc, rule["name"], now, now),
                )
                conn.execute(
                    """INSERT OR REPLACE INTO rule_versions
             (rule_version_id, rule_id, version, change_log, status, approved_by, created_at)
             VALUES (?, ?, ?, ?, 'Frozen', NULL, ?)""",
                    (
                        f"{rid}_v1.0.0",
                        rid,
                        catalog_version,
                        f"Frozen catalog v{catalog_version} ({doc_ref})",
                        now,
                    ),
                )
                conn.execute(
                    """INSERT OR REPLACE INTO rule_lifecycle
             (lifecycle_id, rule_id, stage, started_at, completed_at)
             VALUES (?, ?, 'Idea', ?, NULL)""",
                    (f"{rid}_lifecycle", rid, now),
                )
                conn.execute(
                    "INSERT OR REPLACE INTO rule_tags (tag_id, rule_id, tag) VALUES (?, ?, ?)",
                    (str(uuid.uuid4()), rid, "Catalog"),
                )

    def _seed_composite_catalog(
        self,
        conn: sqlite3.Connection,
        now: str,
        path: Path,
        catalog: dict[str, Any],
    ) -> None:
        """Load frozen composite rule library (TASS-027). Registry entries take precedence."""
        catalog_version = catalog.get("catalog_version", "1.0")
        doc_ref = path.stem.replace("_", " ").upper()
        for comp_cat in catalog.get("composite_categories") or []:
            atomic_cat = comp_cat.get("atomic_category")
            comp_code = comp_cat.get("code", "")
            if not atomic_cat:
                continue
            for sub in comp_cat.get("subcategories") or []:
                sub_name = sub["name"]
                sc = _subcategory_code(atomic_cat, sub_name)
                conn.execute(
                    """INSERT OR REPLACE INTO subcategories
             (subcategory_code, category_code, subcategory_name, description, display_order, enabled)
             VALUES (?, ?, ?, ?, ?, 1)""",
                    (sc, atomic_cat, sub_name, sub_name, 1),
                )
                for rule in sub.get("rules") or []:
                    rid = to_canonical_id(rule["id"])
                    existing = conn.execute(
                        "SELECT rule_id FROM rules WHERE rule_id = ?", (rid,)
                    ).fetchone()
                    if existing:
                        continue
                    conn.execute(
                        """INSERT INTO rules
               (rule_id, rule_name, category_code, subcategory_code, current_version, status,
                priority, weight, description, author, rule_type, spec_path, implementation_path,
                created_at, updated_at)
               VALUES (?, ?, ?, ?, '1.0.0', 'Frozen', 'Medium', 1.0, ?, 'TASS Project', 'composite',
                       '', '', ?, ?)""",
                        (rid, rule["name"], atomic_cat, sc, rule["name"], now, now),
                    )
                    conn.execute(
                        """INSERT OR REPLACE INTO rule_versions
               (rule_version_id, rule_id, version, change_log, status, approved_by, created_at)
               VALUES (?, ?, ?, ?, 'Frozen', NULL, ?)""",
                        (
                            f"{rid}_v1.0.0",
                            rid,
                            catalog_version,
                            f"Frozen composite library v{catalog_version} ({doc_ref})",
                            now,
                        ),
                    )
                    conn.execute(
                        """INSERT OR REPLACE INTO rule_lifecycle
               (lifecycle_id, rule_id, stage, started_at, completed_at)
               VALUES (?, ?, 'Idea', ?, NULL)""",
                        (f"{rid}_lifecycle", rid, now),
                    )
                    for tag in ("Catalog", "Composite", comp_code):
                        conn.execute(
                            "INSERT OR REPLACE INTO rule_tags (tag_id, rule_id, tag) VALUES (?, ?, ?)",
                            (str(uuid.uuid4()), rid, tag),
                        )

    def _upsert_rule_from_meta(
        self, conn: sqlite3.Connection, rule_id: str, meta: dict[str, Any], now: str
    ) -> None:
        rid = to_canonical_id(rule_id)
        cat = parse_category_from_rule_id(rid).value
        sub_name = meta.get("subcategory", "General")
        sc = _subcategory_code(cat, sub_name)
        conn.execute(
            """INSERT OR IGNORE INTO subcategories
         (subcategory_code, category_code, subcategory_name, description, display_order, enabled)
         VALUES (?, ?, ?, ?, 99, 1)""",
            (sc, cat, sub_name, sub_name),
        )
        rtype = parse_rule_type(rid).value
        impl = meta.get("class") or meta.get("function", "")
        conn.execute(
            """INSERT OR REPLACE INTO rules
         (rule_id, rule_name, category_code, subcategory_code, current_version, status,
          priority, weight, description, author, rule_type, spec_path, implementation_path,
          created_at, updated_at)
         VALUES (?, ?, ?, ?, '1.0.0', ?, ?, ?, ?, 'TASS Project', ?, ?, ?, ?, ?)""",
            (
                rid,
                meta["name"],
                cat,
                sc,
                meta.get("status", "Draft"),
                meta.get("priority", "Medium"),
                float(meta.get("weight", 1.0)),
                meta.get("description", meta["name"]),
                rtype,
                meta.get("spec", ""),
                impl,
                now,
                now,
            ),
        )
        conn.execute(
            """INSERT OR REPLACE INTO rule_versions
         (rule_version_id, rule_id, version, change_log, status, approved_by, created_at)
         VALUES (?, ?, '1.0.0', 'Initial seed from registry.yaml', ?, NULL, ?)""",
            (f"{rid}_v1.0.0", rid, meta.get("status", "Draft"), now),
        )
        stage = "Implemented" if rid == "TR0001" else meta.get("status", "Draft")
        conn.execute(
            """INSERT OR REPLACE INTO rule_lifecycle
         (lifecycle_id, rule_id, stage, started_at, completed_at)
         VALUES (?, ?, ?, ?, NULL)""",
            (f"{rid}_lifecycle", rid, stage, now),
        )
        for dep in meta.get("dependencies") or []:
            dep_id = to_canonical_id(dep)
            conn.execute(
                """INSERT OR REPLACE INTO rule_dependencies
           (dependency_id, rule_id, depends_on_rule, dependency_type)
           VALUES (?, ?, ?, 'Required')""",
                (f"{rid}_dep_{dep_id}", rid, dep_id),
            )
        for lid in meta.get("legacy_ids") or []:
            conn.execute(
                "INSERT OR REPLACE INTO rule_aliases (alias_id, rule_id, alias) VALUES (?, ?, ?)",
                (str(uuid.uuid4()), rid, lid),
            )
        if rid == "TR0001":
            self._seed_tr0001_details(conn, rid)

    def _seed_tr0001_details(self, conn: sqlite3.Connection, rid: str) -> None:
        params = [
            ("lookback", "Integer", "40", "20", "120", 1, "Trading days window"),
            ("pivot_strength", "Integer", "3", "2", "5", 1, "Pivot detection strength"),
            ("min_hh_count", "Integer", "2", "1", "5", 1, "Minimum higher-high count"),
        ]
        for name, ptype, default, mn, mx, req, desc in params:
            conn.execute(
                """INSERT OR REPLACE INTO rule_parameters
           (parameter_id, rule_id, parameter_name, parameter_type, default_value,
            minimum, maximum, required, description)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (f"{rid}_param_{name}", rid, name, ptype, default, mn, mx, req, desc),
            )
        for name, itype, req, desc in [
            ("high", "Series", 1, "High price series"),
            ("close", "Series", 1, "Close price series"),
            ("volume", "Series", 0, "Volume series"),
        ]:
            conn.execute(
                """INSERT OR REPLACE INTO rule_inputs
           (input_id, rule_id, input_name, input_type, required, description)
           VALUES (?, ?, ?, ?, ?, ?)""",
                (f"{rid}_in_{name}", rid, name, itype, req, desc),
            )
        for name, otype, desc in [
            ("verdict", "Enum", "PASS | FAIL | UNKNOWN"),
            ("score", "Float", "0-20"),
            ("metadata", "Object", "Explainability payload"),
        ]:
            conn.execute(
                """INSERT OR REPLACE INTO rule_outputs
           (output_id, rule_id, output_name, output_type, description)
           VALUES (?, ?, ?, ?, ?)""",
                (f"{rid}_out_{name}", rid, name, otype, desc),
            )
        for tag in ("Trend", "Bullish", "Core", "Direction"):
            conn.execute(
                "INSERT OR REPLACE INTO rule_tags (tag_id, rule_id, tag) VALUES (?, ?, ?)",
                (str(uuid.uuid4()), rid, tag),
            )
        conn.execute(
            """INSERT OR REPLACE INTO rule_tests
         (test_id, rule_id, test_name, test_type, status, coverage, last_run)
         VALUES (?, ?, ?, 'Unit', 'Pass', 1.0, ?)""",
            (f"{rid}_test_unit", rid, "test_trend_rules", _utc_now()),
        )

    def _sync_rule_folders(self) -> None:
        """Ensure per-rule folder exists with metadata.json."""
        for record in self.all_rules():
            folder = DB_DIR / "rules" / record.rule_id
            folder.mkdir(parents=True, exist_ok=True)
            meta_path = folder / "metadata.json"
            if not meta_path.exists():
                meta_path.write_text(
                    json.dumps(
                        {
                            "rule_id": record.rule_id,
                            "rule_name": record.rule_name,
                            "category": record.category_code,
                            "subcategory": record.subcategory_name,
                            "version": record.current_version,
                            "status": record.status,
                            "priority": record.priority,
                            "weight": record.weight,
                            "description": record.description,
                            "inputs": record.inputs,
                            "outputs": record.outputs,
                            "dependencies": [d["depends_on_rule"] for d in record.dependencies],
                            "tags": record.tags,
                        },
                        indent=2,
                        ensure_ascii=False,
                    ),
                    encoding="utf-8",
                )

    def resolve(self, rule_id: str) -> str:
        conn = self._connect()
        cid = to_canonical_id(rule_id)
        row = conn.execute("SELECT rule_id FROM rules WHERE rule_id = ?", (cid,)).fetchone()
        if row:
            return row["rule_id"]
        alias = conn.execute(
            "SELECT rule_id FROM rule_aliases WHERE alias = ?", (rule_id,)
        ).fetchone()
        if alias:
            return alias["rule_id"]
        return to_canonical_id(rule_id)

    def get_rule(self, rule_id: str) -> RuleRecord | None:
        rid = self.resolve(rule_id)
        conn = self._connect()
        row = conn.execute("SELECT * FROM rules WHERE rule_id = ?", (rid,)).fetchone()
        if not row:
            return None
        sub = conn.execute(
            "SELECT subcategory_name FROM subcategories WHERE subcategory_code = ?",
            (row["subcategory_code"],),
        ).fetchone()
        params = [
            dict(r) for r in conn.execute("SELECT * FROM rule_parameters WHERE rule_id = ?", (rid,))
        ]
        inputs = [
            dict(r) for r in conn.execute("SELECT * FROM rule_inputs WHERE rule_id = ?", (rid,))
        ]
        outputs = [
            dict(r) for r in conn.execute("SELECT * FROM rule_outputs WHERE rule_id = ?", (rid,))
        ]
        deps = [
            dict(r)
            for r in conn.execute("SELECT * FROM rule_dependencies WHERE rule_id = ?", (rid,))
        ]
        tags = [
            r["tag"] for r in conn.execute("SELECT tag FROM rule_tags WHERE rule_id = ?", (rid,))
        ]
        lc = conn.execute(
            "SELECT stage FROM rule_lifecycle WHERE rule_id = ? ORDER BY started_at DESC LIMIT 1",
            (rid,),
        ).fetchone()
        return RuleRecord(
            rule_id=row["rule_id"],
            rule_name=row["rule_name"],
            category_code=row["category_code"],
            subcategory_code=row["subcategory_code"],
            subcategory_name=sub["subcategory_name"] if sub else "",
            current_version=row["current_version"],
            status=row["status"],
            priority=row["priority"],
            weight=row["weight"],
            description=row["description"] or "",
            author=row["author"],
            rule_type=row["rule_type"],
            spec_path=row["spec_path"] or "",
            implementation_path=row["implementation_path"] or "",
            parameters=params,
            inputs=inputs,
            outputs=outputs,
            dependencies=deps,
            tags=tags,
            lifecycle_stage=lc["stage"] if lc else "Draft",
            folder_path=str(DB_DIR / "rules" / rid),
        )

    def all_rules(self) -> list[RuleRecord]:
        rows = self._connect().execute("SELECT rule_id FROM rules ORDER BY rule_id").fetchall()
        return [r for row in rows if (r := self.get_rule(row["rule_id"]))]

    def list_categories(self) -> list[str]:
        rows = (
            self._connect()
            .execute("SELECT category_code FROM categories ORDER BY display_order")
            .fetchall()
        )
        return [r["category_code"] for r in rows]

    def search(self, **filters: Any) -> list[RuleRecord]:
        clauses: list[str] = []
        params: list[Any] = []
        for key, val in filters.items():
            if val is None:
                continue
            if key == "tag":
                clauses.append("rule_id IN (SELECT rule_id FROM rule_tags WHERE tag = ?)")
                params.append(val)
            elif key in ("category_code", "subcategory_code", "status", "priority", "rule_id"):
                clauses.append(f"{key} = ?")
                params.append(val)
        sql = "SELECT rule_id FROM rules"
        if clauses:
            sql += " WHERE " + " AND ".join(clauses)
        sql += " ORDER BY rule_id"
        rows = self._connect().execute(sql, params).fetchall()
        return [r for row in rows if (r := self.get_rule(row["rule_id"]))]

    def validate_rule(self, rule_id: str) -> tuple[bool, list[str]]:
        errors: list[str] = []
        rid = self.resolve(rule_id)
        record = self.get_rule(rid)
        if not record:
            return False, [f"Rule not found: {rule_id}"]
        if not record.category_code:
            errors.append("Missing category")
        if not record.subcategory_code:
            errors.append("Missing subcategory")
        if record.weight <= 0:
            errors.append("Invalid weight")
        if self._has_circular_dependency(rid):
            errors.append("Circular dependency detected")
        for dep in record.dependencies:
            if not self.get_rule(dep["depends_on_rule"]):
                errors.append(f"Invalid dependency: {dep['depends_on_rule']}")
        folder = Path(record.folder_path)
        if not folder.exists():
            errors.append(f"Missing rule folder: {folder}")
        return len(errors) == 0, errors

    def _has_circular_dependency(self, rule_id: str, visiting: set[str] | None = None) -> bool:
        visiting = visiting or set()
        if rule_id in visiting:
            return True
        visiting.add(rule_id)
        record = self.get_rule(rule_id)
        if not record:
            return False
        for dep in record.dependencies:
            if self._has_circular_dependency(dep["depends_on_rule"], visiting.copy()):
                return True
        return False

    def upsert_from_folder(self, rule_id: str) -> bool:
        """Insert or update a rule row from ``rule_database/rules/{id}/metadata.json``."""
        rid = to_canonical_id(rule_id)
        folder = DB_DIR / "rules" / rid
        meta_path = folder / "metadata.json"
        if not meta_path.exists():
            return False

        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        cat = meta.get("category") or parse_category_from_rule_id(rid).value
        sub_name = meta.get("subcategory") or "General"
        sc = _subcategory_code(cat, sub_name)
        now = _utc_now()
        conn = self._connect()

        conn.execute(
            """INSERT OR REPLACE INTO categories
         (category_code, category_name, description, display_order, enabled, created_at, updated_at)
         VALUES (?, ?, ?, 99, 1, ?, ?)""",
            (cat, CATEGORY_NAMES.get(CategoryCode(cat), cat), f"{cat} rules", now, now),
        )
        conn.execute(
            """INSERT OR REPLACE INTO subcategories
         (subcategory_code, category_code, subcategory_name, description, display_order, enabled)
         VALUES (?, ?, ?, ?, 99, 1)""",
            (sc, cat, sub_name, sub_name),
        )

        rtype = parse_rule_type(rid).value
        conn.execute(
            """INSERT OR REPLACE INTO rules
         (rule_id, rule_name, category_code, subcategory_code, current_version, status,
          priority, weight, description, author, rule_type, spec_path, implementation_path,
          created_at, updated_at)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'TASS Project', ?, ?, ?, ?, ?)""",
            (
                rid,
                meta.get("rule_name", rid),
                cat,
                sc,
                meta.get("version", "1.0.0"),
                meta.get("status", "Frozen"),
                meta.get("priority", "Medium"),
                float(meta.get("weight", 1.0)),
                meta.get("description", meta.get("rule_name", rid)),
                rtype,
                str(folder / "specification.md"),
                meta.get("implementation", ""),
                meta.get("created_at", now),
                now,
            ),
        )
        conn.commit()
        return True

    def set_lifecycle_stage(self, rule_id: str, stage: str) -> None:
        """Append a lifecycle stage transition for a rule."""
        rid = to_canonical_id(rule_id)
        if self.get_rule(rid) is None:
            self.upsert_from_folder(rid)
        if self.get_rule(rid) is None:
            raise ValueError(f"Rule not found and folder sync failed: {rid}")

        now = _utc_now()
        self._connect().execute(
            """INSERT INTO rule_lifecycle
         (lifecycle_id, rule_id, stage, started_at, completed_at)
         VALUES (?, ?, ?, ?, NULL)""",
            (f"{rid}_{stage}_{uuid.uuid4().hex[:8]}", rid, stage, now),
        )
        self._connect().commit()
        self.record_history(rid, "lifecycle_stage", "", stage, changed_by="mvp_ssot")

    def record_history(
        self,
        rule_id: str,
        field: str,
        old_value: str,
        new_value: str,
        changed_by: str = "system",
        version: str = "1.0.0",
    ) -> None:
        rid = self.resolve(rule_id)
        self._connect().execute(
            """INSERT INTO rule_history
         (history_id, rule_id, version, field, old_value, new_value, changed_by, changed_at)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (str(uuid.uuid4()), rid, version, field, old_value, new_value, changed_by, _utc_now()),
        )
        self._connect().commit()


_default_db: RuleDatabase | None = None


def get_rule_database() -> RuleDatabase:
    global _default_db
    if _default_db is None:
        _default_db = RuleDatabase()
    return _default_db
