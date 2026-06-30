#!/usr/bin/env python3
"""Finalize REVISE/INSUFFICIENT MVP rules to Rejected (TASS-009 accuracy-first)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.core.adopted_rules import clear_adopted_rules_cache
from engine.core.mvp_adoption import finalize_non_adopted_rules


def main() -> int:
    parser = argparse.ArgumentParser(description="Finalize non-Adopted MVP rules to Rejected")
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("output/mvp_adoption_report.json"),
    )
    parser.add_argument("--output", type=Path, default=Path("output/mvp_adoption_finalized.json"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.report.exists():
        print(json.dumps({"passed": False, "error": f"report not found: {args.report}"}, indent=2))
        return 1

    report = json.loads(args.report.read_text(encoding="utf-8"))
    result = finalize_non_adopted_rules(report, dry_run=args.dry_run)
    if not args.dry_run:
        clear_adopted_rules_cache()
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "passed": result["passed"],
                "adopted": result["adopted"],
                "rejected": result["rejected"],
                "dry_run": result["dry_run"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if result.get("passed") else 1


if __name__ == "__main__":
    raise SystemExit(main())
