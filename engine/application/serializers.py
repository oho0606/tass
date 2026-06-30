"""Serialization helpers for Application layer (I/O only)."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from engine.application.types import DailyPicksResult
from engine.core.types import PickResult


def pick_to_dict(pick: PickResult) -> dict[str, object]:
    """Convert ``PickResult`` to JSON-serializable dict.

    Args:
        pick: Ranked pick from recommendation pipeline.

    Returns:
        Dictionary suitable for JSON export.
    """
    return {
        "rank": pick.rank,
        "symbol": pick.symbol,
        "name": pick.name,
        "total_score": pick.total_score,
        "max_score": pick.max_score,
        "domains": pick.domains,
        "confidence": pick.confidence,
        "risk": pick.risk,
        "reasons": pick.reasons,
        "gate": pick.gate,
        "grade": pick.grade,
        "probability": pick.probability,
        "probability_grade": pick.probability_grade,
        "probability_level": pick.probability_level,
        "confidence_grade": pick.confidence_grade,
        "confidence_level": pick.confidence_level,
        "confidence_stars": pick.confidence_stars,
        "risk_grade": pick.risk_grade,
        "risk_grade_stars": pick.risk_grade_stars,
        "risk_level": pick.risk_level,
        "risk_decision": pick.risk_decision,
        "risk_breakdown": pick.risk_breakdown,
        "recommendation": pick.recommendation,
        "recommendation_grade": pick.recommendation_grade,
        "recommendation_reason": pick.recommendation_reason,
        "passed_conditions": pick.passed_conditions,
        "failed_conditions": pick.failed_conditions,
        "gate_report": pick.gate_report,
        "composite_breakdown": pick.composite_breakdown,
    }


def daily_picks_to_payload(result: DailyPicksResult) -> dict[str, object]:
    """Convert daily picks result to JSON payload."""
    payload: dict[str, object] = {
        "date": result.date,
        "mvp_mode": result.mvp_mode,
        "generated_at": result.generated_at,
        "universe_size": result.universe_size,
        "candidates_evaluated": result.candidates_evaluated,
        "picks": [pick_to_dict(pick) for pick in result.picks],
    }
    if result.gate_blocked:
        payload["gate_blocked"] = [pick_to_dict(pick) for pick in result.gate_blocked]
    return payload


def save_daily_picks_json(result: DailyPicksResult, output_dir: Path) -> Path:
    """Persist daily picks to ``picks_YYYY-MM-DD.json``.

    Args:
        result: Generated picks result.
        output_dir: Target directory.

    Returns:
        Path to written JSON file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"picks_{result.date}.json"
    payload = daily_picks_to_payload(result)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
    return path


def format_daily_picks_summary(result: DailyPicksResult) -> str:
    """Build human-readable CLI summary for daily picks."""
    lines = [f"TASS Top {len(result.picks)} Picks — {result.date}", "-" * 60]
    for pick in result.picks:
        grade = pick.grade or "-"
        gate = pick.gate or "PASS"
        lines.append(
            f"{pick.rank:2}. {pick.name} ({pick.symbol})  "
            f"{pick.total_score:.0f}/{pick.max_score:.0f}  [{grade}] gate={gate}"
        )
    if result.gate_blocked:
        lines.append("")
        lines.append(f"Gate Blocked ({len(result.gate_blocked)} observation)")
        for pick in result.gate_blocked:
            reason = (pick.reasons or ["Pipeline gate FAIL"])[0]
            lines.append(
                f"  - {pick.name} ({pick.symbol})  {pick.total_score:.0f}  {reason}"
            )
    if result.output_path is not None:
        lines.append(f"\nSaved: {result.output_path}")
    return "\n".join(lines)
