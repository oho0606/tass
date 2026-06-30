from __future__ import annotations

from typing import Any, Dict

from engine.gate.models import GateResult, GateStatus


def evaluate_data_quality_gate(data: Dict[str, Any], config: Dict[str, Any]) -> GateResult:
    """데이터 검증 및 최소 히스토리 길이 평가."""
    dq_config = config.get("data_quality", {})

    if not data.get("data_valid", True):
        return GateResult(
            name="DataQualityGate",
            status=GateStatus.FAIL,
            reason="Data validation failed.",
        )

    min_bars = dq_config.get("min_bars", 60)
    bar_count = data.get("bar_count", 0)
    if bar_count < min_bars:
        return GateResult(
            name="DataQualityGate",
            status=GateStatus.FAIL,
            reason=f"Insufficient history ({bar_count} < {min_bars}).",
        )

    return GateResult(
        name="DataQualityGate",
        status=GateStatus.PASS,
        reason="Data quality is acceptable.",
    )
