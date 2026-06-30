"""MVP rule adoption finalization (TASS-009)."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from engine.core.rule_database import RuleDatabase

RULE_DB_DIR = Path("rule_database/rules")


def _utc_now() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def finalize_non_adopted_rules(
    report: dict,
    *,
    dry_run: bool = False,
) -> dict:
    """Promote REVISE/Implemented rules to Rejected lifecycle (accuracy-first)."""
    db = RuleDatabase()
    finalized: list[dict] = []

    for rule in report.get("rules") or []:
        rule_id = rule.get("rule_id")
        if not rule_id:
            continue
        lifecycle = rule.get("lifecycle")
        aggregate = rule.get("aggregate_verdict")
        if lifecycle in {"Adopted", "Rejected"}:
            finalized.append(
                {"rule_id": rule_id, "action": "keep", "lifecycle": lifecycle, "aggregate": aggregate}
            )
            continue

        reason = (
            f"Aggregate backtest verdict {aggregate} — not promoted to Adopted "
            f"(TASS-009: rules not passing backtest must not be adopted)."
        )
        meta_path = RULE_DB_DIR / rule_id / "metadata.json"
        if meta_path.exists() and not dry_run:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            meta["lifecycle_stage"] = "Rejected"
            meta["backtest_verdict"] = "REJECT"
            meta["rejection_reason"] = reason
            meta["finalized_at"] = _utc_now()
            meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            db.set_lifecycle_stage(rule_id, "Rejected")

        rule["lifecycle"] = "Rejected"
        rule["aggregate_verdict"] = "REJECT"
        finalized.append(
            {
                "rule_id": rule_id,
                "action": "reject",
                "lifecycle": "Rejected",
                "aggregate": aggregate,
                "reason": reason,
            }
        )

    adopted = sum(1 for item in finalized if item["lifecycle"] == "Adopted")
    rejected = sum(1 for item in finalized if item["lifecycle"] == "Rejected")
    db.close()

    summary = {
        "passed": adopted > 0 and adopted + rejected == len(finalized),
        "adopted": adopted,
        "rejected": rejected,
        "rules": finalized,
        "dry_run": dry_run,
    }
    report["adopted"] = adopted
    report["rejected"] = rejected
    report["finalized"] = summary
    return summary
