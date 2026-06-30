from __future__ import annotations

from typing import Any, Dict

from engine.gate.models import GateResult, GateStatus


def evaluate_volatility_gate(data: Dict[str, Any], config: Dict[str, Any]) -> GateResult:
    """종목의 변동성 평가 (ATR, BB Width)"""
    vol_config = config.get("volatility", {})
    atr_percent = data.get("atr_percent", 0.0)

    fail_threshold = vol_config.get("fail_threshold", 0.15)
    warn_threshold = vol_config.get("warn_threshold", 0.10)
    penalty = vol_config.get("warning_penalty", 15)

    if atr_percent >= fail_threshold:
        return GateResult(
            "VolatilityGate",
            GateStatus.FAIL,
            f"Extreme volatility: ATR% {atr_percent:.2f}",
        )
    elif atr_percent >= warn_threshold:
        return GateResult(
            "VolatilityGate",
            GateStatus.WARNING,
            f"High volatility: ATR% {atr_percent:.2f}",
            deduction=penalty,
        )

    return GateResult("VolatilityGate", GateStatus.PASS, "Normal volatility.")
