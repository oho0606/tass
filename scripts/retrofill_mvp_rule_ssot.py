#!/usr/bin/env python3
"""Retrofill TASS-013 SSOT files for MVP operational rules."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
RULE_DB = ROOT / "rule_database" / "rules"
CATALOG_DIR = ROOT / "rules" / "catalog"
MVP_CONFIG = ROOT / "config" / "mvp_operational_rules.yaml"

CATALOG_DOCS = {
    "TR": "docs/TASS-014_TR_Rule_Catalog_v1.0.md",
    "MA": "docs/TASS-015_MA_Rule_Catalog_v1.0.md",
    "VL": "docs/TASS-017_VL_Rule_Catalog_v1.0.md",
    "CTR": "docs/TASS-027_Composite_Rule_Library_v1.0.md",
}


def _utc_today() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d")


def _load_mvp_rule_ids() -> list[str]:
    with MVP_CONFIG.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    keys = ("trend_atomic", "trend_composite", "moving_average", "volume")
    return [rule_id for key in keys for rule_id in cfg.get(key, [])]


def _load_catalog_index() -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    for path in sorted(CATALOG_DIR.glob("*_v*.yaml")):
        with path.open(encoding="utf-8") as handle:
            catalog = yaml.safe_load(handle) or {}
        if catalog.get("catalog_type") == "composite":
            for comp_cat in catalog.get("composite_categories") or []:
                for sub in comp_cat.get("subcategories") or []:
                    for rule in sub.get("rules") or []:
                        rid = rule["id"].upper()
                        index[rid] = {
                            "name": rule["name"],
                            "category": comp_cat.get("code", rid[:3]),
                            "subcategory": sub["name"],
                            "catalog_file": path.name,
                        }
            continue
        cat_code = catalog.get("category_code", "")
        for sub in catalog.get("subcategories") or []:
            for rule in sub.get("rules") or []:
                rid = rule["id"].upper()
                index[rid] = {
                    "name": rule["name"],
                    "category": cat_code,
                    "subcategory": sub["name"],
                    "catalog_file": path.name,
                }
    return index


def _rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def _find_implementation(rule_id: str) -> str | None:
    if rule_id in {"TR0002", "TR0003", "TR0004"}:
        atomic = ROOT / "engine" / "rules" / "tr" / "atomic.py"
        return _rel(atomic) if atomic.exists() else None

    category_dirs = {
        "TR": ROOT / "engine" / "rules" / "tr",
        "MA": ROOT / "engine" / "rules" / "ma",
        "VL": ROOT / "engine" / "rules" / "vl",
        "CT": ROOT / "engine" / "rules" / "composite",
    }
    cat_key = "CT" if rule_id.startswith("CTR") else rule_id[:2]
    search_dir = category_dirs.get(cat_key)
    if search_dir is None or not search_dir.exists():
        return None

    needle = rule_id.lower()
    for path in sorted(search_dir.rglob("*.py")):
        if needle in path.name.lower():
            return _rel(path)

    if cat_key == "CT":
        composite = ROOT / "engine" / "rules" / "composite" / "ctr.py"
        if composite.exists() and f"class {rule_id}" in composite.read_text(encoding="utf-8"):
            return _rel(composite)
    return None


def _relative_link(from_dir: Path, target: Path) -> str:
    return Path(os_relpath(from_dir, target)).as_posix()


def os_relpath(from_dir: Path, target: Path) -> str:
    try:
        return Path(
            __import__("os").path.relpath(target.resolve(), from_dir.resolve())
        ).as_posix()
    except ValueError:
        return str(target)


def _write_specification(
    rule_dir: Path,
    rule_id: str,
    meta: dict,
    catalog: dict[str, str],
    implementation: str | None,
) -> None:
    cat = catalog.get("category", rule_id[:2])
    catalog_doc = CATALOG_DOCS.get(cat, "docs/TASS-012_Rule_Specification_Standard.md")
    lines = [
        f"# {rule_id} Specification",
        "",
        f"**Rule:** {catalog.get('name', meta.get('rule_name', rule_id))}",
        f"**Category:** {cat} — {catalog.get('subcategory', meta.get('subcategory', ''))}",
        f"**Lifecycle:** MVP Operational (Implemented)",
        "",
        "## Catalog Reference",
        "",
        f"- Frozen catalog: `rules/catalog/{catalog.get('catalog_file', '')}`",
        f"- Human doc: [{catalog_doc}]({os_relpath(rule_dir, ROOT / catalog_doc)})",
        f"- Standard: [TASS-012 Rule Specification Standard]({os_relpath(rule_dir, ROOT / 'docs/TASS-012_Rule_Specification_Standard.md')})",
        "",
        "## Implementation",
        "",
    ]
    if implementation:
        lines.append(f"- Python: `{implementation}`")
    else:
        lines.append("- Python: _pending path resolution_")
    lines.extend(
        [
            "",
            "## MVP Scope",
            "",
            "This rule is part of the frozen MVP operational subset (`config/mvp_operational_rules.yaml`).",
            "Changes require backtest validation before lifecycle promotion to **Adopted**.",
            "",
        ]
    )
    (rule_dir / "specification.md").write_text("\n".join(lines), encoding="utf-8")


def _write_readme(
    rule_dir: Path,
    rule_id: str,
    meta: dict,
    catalog: dict[str, str],
    implementation: str | None,
) -> None:
    name = catalog.get("name", meta.get("rule_name", rule_id))
    lines = [
        f"# {rule_id} — {name}",
        "",
        "Rule Database folder per [TASS-013](../docs/TASS-013_Rule_Database_Specification.md).",
        "",
        "| File | Purpose |",
        "|------|---------|",
        "| `metadata.json` | Machine-readable metadata |",
        "| `parameters.json` | Configurable parameters |",
        "| `specification.md` | MVP operational spec + catalog link |",
        "| `changelog.md` | Version history |",
        "",
    ]
    if implementation:
        lines.append(f"**Implementation:** `{implementation}`")
    lines.append("")
    lines.append("**MVP status:** Operational subset — see `config/mvp_operational_rules.yaml`")
    (rule_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def _write_changelog(rule_dir: Path, rule_id: str, implementation: str | None) -> None:
    today = _utc_today()
    lines = [
        f"# {rule_id} Changelog",
        "",
        f"## 1.0.0 — {today}",
        "",
        "- MVP SSOT retrofill (`scripts/retrofill_mvp_rule_ssot.py`)",
        "- Lifecycle target: **Implemented** (MVP operational)",
    ]
    if implementation:
        lines.append(f"- Implementation: `{implementation}`")
    (rule_dir / "changelog.md").write_text("\n".join(lines), encoding="utf-8")


def _ensure_parameters(rule_dir: Path, meta: dict) -> None:
    path = rule_dir / "parameters.json"
    if path.exists():
        return
    payload = {
        "rule_id": meta.get("rule_id", rule_dir.name),
        "version": meta.get("version", "1.0.0"),
        "parameters": [],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _update_metadata(rule_dir: Path, meta: dict, implementation: str | None) -> None:
    meta = dict(meta)
    meta["mvp_operational"] = True
    meta["lifecycle_stage"] = "Implemented"
    meta["updated_at"] = _utc_today()
    if implementation:
        meta["implementation"] = implementation
    (rule_dir / "metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def retrofill_rule(rule_id: str, catalog_index: dict[str, dict[str, str]], dry_run: bool) -> bool:
    rule_dir = RULE_DB / rule_id
    if not rule_dir.exists():
        print(f"SKIP {rule_id}: folder missing")
        return False

    meta_path = rule_dir / "metadata.json"
    meta = {}
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    meta.setdefault("rule_id", rule_id)

    catalog = catalog_index.get(rule_id, {})
    implementation = _find_implementation(rule_id)

    if dry_run:
        print(f"DRY {rule_id}: impl={implementation}")
        return True

    _write_specification(rule_dir, rule_id, meta, catalog, implementation)
    _write_readme(rule_dir, rule_id, meta, catalog, implementation)
    _write_changelog(rule_dir, rule_id, implementation)
    _ensure_parameters(rule_dir, meta)
    _update_metadata(rule_dir, meta, implementation)
    print(f"OK   {rule_id}")
    return True


def update_db_lifecycle(rule_ids: list[str], stage: str) -> int:
    from engine.core.rule_database import RuleDatabase

    db = RuleDatabase()
    updated = 0
    for rule_id in rule_ids:
        try:
            db.set_lifecycle_stage(rule_id, stage)
            updated += 1
        except Exception as exc:  # noqa: BLE001 — report per-rule failures
            print(f"DB  {rule_id}: {exc}")
    db.close()
    return updated


def main() -> int:
    parser = argparse.ArgumentParser(description="Retrofill MVP rule SSOT files")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-db", action="store_true", help="Skip lifecycle DB update")
    args = parser.parse_args()

    with MVP_CONFIG.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    rule_ids = _load_mvp_rule_ids()
    catalog_index = _load_catalog_index()

    ok = sum(1 for rid in rule_ids if retrofill_rule(rid, catalog_index, args.dry_run))
    print(f"Retrofilled {ok}/{len(rule_ids)} MVP rules")

    if not args.dry_run and not args.skip_db:
        stage = cfg.get("lifecycle_target", "Implemented")
        count = update_db_lifecycle(rule_ids, stage)
        print(f"Lifecycle updated: {count} rules → {stage}")

    return 0 if ok == len(rule_ids) else 1


if __name__ == "__main__":
    raise SystemExit(main())
