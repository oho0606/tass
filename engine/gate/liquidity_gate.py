from __future__ import annotations

from typing import Any, Dict

import pandas as pd

from engine.gate.models import GateResult, GateStatus


def evaluate_liquidity_gate(data: Dict[str, Any], config: Dict[str, Any]) -> GateResult:
    """평균 거래대금 기반 유동성 평가."""
    liq_config = config.get("liquidity", {})
    traded_value_ma20 = data.get("traded_value_ma20")
    min_traded_value = liq_config.get("min_traded_value_ma20", 500_000_000)

    if traded_value_ma20 is None or pd.isna(traded_value_ma20):
        return GateResult(
            name="LiquidityGate",
            status=GateStatus.FAIL,
            reason="Missing traded value data.",
        )

    if float(traded_value_ma20) < min_traded_value:
        return GateResult(
            name="LiquidityGate",
            status=GateStatus.FAIL,
            reason=f"Insufficient liquidity (MA20 traded value {float(traded_value_ma20):,.0f} < {min_traded_value:,.0f}).",
        )

    return GateResult(
        name="LiquidityGate",
        status=GateStatus.PASS,
        reason="Liquidity is sufficient.",
    )
