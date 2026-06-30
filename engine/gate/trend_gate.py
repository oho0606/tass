from __future__ import annotations

from typing import Any, Dict

from engine.gate.models import GateResult, GateStatus


def evaluate_trend_gate(data: Dict[str, Any], config: Dict[str, Any]) -> GateResult:
    """장기 추세 점수 기반 Trend Gate 평가."""
    trend_config = config.get("trend", {})
    trend_score = data.get("trend_score", 0.0)
    floor_score = trend_config.get("floor_score", 120.0)

    if trend_score < floor_score:
        return GateResult(
            name="TrendGate",
            status=GateStatus.FAIL,
            reason=f"Trend score below floor ({trend_score:.0f} < {floor_score:.0f}).",
        )

    return GateResult(
        name="TrendGate",
        status=GateStatus.PASS,
        reason="Trend condition is acceptable.",
    )
