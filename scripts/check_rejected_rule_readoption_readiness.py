#!/usr/bin/env python3
"""Check whether rejected MVP rules are ready for re-adoption backtests."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def _parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check_readiness(status_path: Path) -> dict[str, Any]:
    status = _load_json(status_path)
    rejected = status.get("rejected_rules") or []
    rows: list[dict[str, Any]] = []

    ready_count = 0
    for item in rejected:
        rule_id = str(item.get("rule_id", "")).strip()
        meta_path = ROOT / "rule_database" / "rules" / rule_id / "metadata.json"
        if not rule_id or not meta_path.exists():
            rows.append(
                {
                    "rule_id": rule_id or "(missing)",
                    "ready_for_rebacktest": False,
                    "reason": "metadata_missing",
                    "metadata_path": str(meta_path),
                }
            )
            continue

        meta = _load_json(meta_path)
        lifecycle = str(meta.get("lifecycle_stage", ""))
        finalized_at = _parse_iso(meta.get("finalized_at"))
        updated_at = _parse_iso(meta.get("updated_at"))
        backtest_eval_at = _parse_iso(meta.get("backtest_evaluated_at"))

        revised_since_reject = bool(updated_at and finalized_at and updated_at > finalized_at)
        retested_since_reject = bool(backtest_eval_at and finalized_at and backtest_eval_at > finalized_at)
        lifecycle_reopened = lifecycle in {"Draft", "Frozen", "Implemented"}
        ready = lifecycle_reopened and revised_since_reject and retested_since_reject
        if ready:
            ready_count += 1

        rows.append(
            {
                "rule_id": rule_id,
                "lifecycle_stage": lifecycle,
                "ready_for_rebacktest": ready,
                "revised_since_reject": revised_since_reject,
                "retested_since_reject": retested_since_reject,
                "backtest_verdict": meta.get("backtest_verdict"),
                "metadata_path": str(meta_path),
            }
        )

    return {
        "status_path": str(status_path),
        "total_rejected": len(rows),
        "ready_count": ready_count,
        "not_ready_count": len(rows) - ready_count,
        "rules": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check rejected-rule re-adoption readiness")
    parser.add_argument(
        "--status",
        type=Path,
        default=Path("output/rejected_rules_status.json"),
        help="Rejected-rule status manifest path",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/rejected_rules_readiness.json"),
        help="Readiness report output path",
    )
    args = parser.parse_args()

    report = check_readiness(args.status)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ready_count"] > 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
