#!/usr/bin/env python3
"""Verify 3-way mapping: catalog ↔ rule_database SSOT ↔ engine implementation."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
RULE_DB = ROOT / "rule_database" / "rules"
MVP_CONFIG = ROOT / "config" / "mvp_operational_rules.yaml"


def _load_mvp_rule_ids() -> list[str]:
    with MVP_CONFIG.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    keys = ("trend_atomic", "trend_composite", "moving_average", "volume")
    return [rule_id for key in keys for rule_id in cfg.get(key, [])]


def _find_implementation(rule_id: str) -> Path | None:
    if rule_id in {"TR0002", "TR0003", "TR0004"}:
        atomic = ROOT / "engine" / "rules" / "tr" / "atomic.py"
        return atomic if atomic.exists() else None

    category_dirs = {
        "TR": ROOT / "engine" / "rules" / "tr",
        "MA": ROOT / "engine" / "rules" / "ma",
        "VL": ROOT / "engine" / "rules" / "vl",
        "CT": ROOT / "engine" / "rules" / "composite",
    }
    cat_key = "CT" if rule_id.startswith("CTR") else rule_id[:2]
    search_dir = category_dirs.get(cat_key)
    if search_dir is None:
        return None
    needle = rule_id.lower()
    for path in sorted(search_dir.rglob("*.py")):
        if needle in path.name.lower():
            return path
    if cat_key == "CT":
        composite = ROOT / "engine" / "rules" / "composite" / "ctr.py"
        if composite.exists() and f"class {rule_id}" in composite.read_text(encoding="utf-8"):
            return composite
    return None


def _check_evaluator_registered(rule_id: str) -> bool:
    try:
        if rule_id.startswith("CTR"):
            from engine.rules.composite.registry import COMPOSITE_EVALUATORS

            return rule_id in COMPOSITE_EVALUATORS
        prefix = rule_id[:2]
        if prefix == "TR":
            from engine.rules.tr.registry import TR_EVALUATORS

            return rule_id in TR_EVALUATORS
        if prefix == "MA":
            from engine.rules.ma.registry import MA_EVALUATORS

            return rule_id in MA_EVALUATORS
        if prefix == "VL":
            from engine.rules.vl.registry import VL_EVALUATORS

            return rule_id in VL_EVALUATORS
    except Exception:
        return False
    return False


def verify_rule(rule_id: str) -> list[str]:
    errors: list[str] = []
    rule_dir = RULE_DB / rule_id
    if not rule_dir.is_dir():
        errors.append(f"{rule_id}: missing rule_database folder")
        return errors

    for filename in ("metadata.json", "specification.md", "README.md", "changelog.md"):
        if not (rule_dir / filename).exists():
            errors.append(f"{rule_id}: missing {filename}")

    impl = _find_implementation(rule_id)
    if impl is None:
        errors.append(f"{rule_id}: no engine implementation file")

    if rule_id.startswith("CTR"):
        if not _check_evaluator_registered(rule_id):
            errors.append(f"{rule_id}: not in composite registry")
    elif not _check_evaluator_registered(rule_id):
        errors.append(f"{rule_id}: not in category registry")

    meta_path = rule_dir / "metadata.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if not meta.get("mvp_operational"):
            errors.append(f"{rule_id}: metadata.mvp_operational not set")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify MVP rule SSOT 3-way mapping")
    parser.add_argument("--all-mvp", action="store_true", default=True)
    args = parser.parse_args()

    rule_ids = _load_mvp_rule_ids()
    all_errors: list[str] = []
    for rule_id in rule_ids:
        all_errors.extend(verify_rule(rule_id))

    if all_errors:
        print("SSOT verification FAILED:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(f"SSOT verification PASSED ({len(rule_ids)} MVP operational rules)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
