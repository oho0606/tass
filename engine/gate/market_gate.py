from __future__ import annotations

from typing import Any, Dict

from engine.gate.market_context import resolve_effective_market_trend
from engine.gate.models import GateResult, GateStatus


def evaluate_market_gate(data: Dict[str, Any], config: Dict[str, Any]) -> GateResult:
    """시장 전체의 상태를 평가 (KOSPI/KOSDAQ)"""
    market_config = config.get("market", {})
    kospi_trend = data.get("kospi_trend", "UP")
    kosdaq_trend = data.get("kosdaq_trend", kospi_trend)
    market_trend = resolve_effective_market_trend(
        kospi_trend=kospi_trend,
        kosdaq_trend=kosdaq_trend,
        listing_market=data.get("listing_market"),
        combine_mode=market_config.get("combine_mode", "worst"),
        market_trend=data.get("market_trend"),
    )
    data["effective_market_trend"] = market_trend

    if market_trend == "CRASH":
        return GateResult(
            name="MarketGate",
            status=GateStatus.FAIL,
            reason="Market is in CRASH state. All buys suspended.",
            deduction=0,
        )
    elif market_trend == "DOWN":
        penalty = market_config.get("warning_penalty", 20)
        return GateResult(
            name="MarketGate",
            status=GateStatus.WARNING,
            reason="Market is in DOWNTREND. Applying penalty.",
            deduction=penalty,
        )

    return GateResult(
        name="MarketGate", status=GateStatus.PASS, reason="Market condition is favorable."
    )
