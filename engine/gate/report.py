from __future__ import annotations

from typing import Any

import pandas as pd

from engine.gate.models import GateResult, GateStatus, PipelineResult

GATE_REPORT_KEYS = {
    "DataQualityGate": ("data_quality", "Data Quality Gate"),
    "MarketGate": ("market", "Market Gate"),
    "LiquidityGate": ("liquidity", "Liquidity Gate"),
    "TrendGate": ("trend", "Trend Gate"),
    "VolatilityGate": ("volatility", "Volatility Gate"),
}


def _format_value(value: Any) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return "N/A"
    if isinstance(value, float):
        if abs(value) >= 1000:
            return f"{value:,.0f}"
        return f"{value:.4f}".rstrip("0").rstrip(".")
    return str(value)


def _threshold_for_gate(gate_name: str, config: dict[str, dict[str, Any]]) -> str:
    if gate_name == "DataQualityGate":
        return f"min_bars={config.get('data_quality', {}).get('min_bars', 60)}"
    if gate_name == "MarketGate":
        market = config.get("market", {})
        mode = market.get("combine_mode", "worst")
        return f"CRASH=FAIL, DOWN=WARNING, combine_mode={mode}"
    if gate_name == "LiquidityGate":
        minimum = config.get("liquidity", {}).get("min_traded_value_ma20", 500_000_000)
        return f"min_traded_value_ma20={minimum:,.0f}"
    if gate_name == "TrendGate":
        floor = config.get("trend", {}).get("floor_score", 120)
        return f"floor_score={floor:.0f}"
    if gate_name == "VolatilityGate":
        vol = config.get("volatility", {})
        return (
            f"warn={vol.get('warn_threshold', 0.10):.2f}, "
            f"fail={vol.get('fail_threshold', 0.15):.2f}"
        )
    return "—"


def _actual_for_gate(gate_name: str, data: dict[str, Any]) -> str:
    if gate_name == "DataQualityGate":
        return f"valid={data.get('data_valid', True)}, bars={data.get('bar_count', 0)}"
    if gate_name == "MarketGate":
        effective = data.get(
            "effective_market_trend",
            data.get("market_trend", data.get("kospi_trend", "UP")),
        )
        listing = data.get("listing_market", "KS")
        return (
            f"KOSPI={data.get('kospi_trend', 'UP')}, "
            f"KOSDAQ={data.get('kosdaq_trend', 'UP')}, "
            f"effective={effective}, listing={listing}"
        )
    if gate_name == "LiquidityGate":
        return f"traded_value_ma20={_format_value(data.get('traded_value_ma20'))}"
    if gate_name == "TrendGate":
        return f"trend_score={_format_value(data.get('trend_score'))}"
    if gate_name == "VolatilityGate":
        return f"atr_percent={_format_value(data.get('atr_percent'))}"
    return "—"


def pipeline_gate_result_to_dict(
    result: GateResult,
    *,
    data: dict[str, Any],
    config: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Convert one pipeline gate result into a pick/report-friendly dict."""
    gate_key, gate_name = GATE_REPORT_KEYS.get(result.name, (result.name, result.name))
    payload: dict[str, Any] = {
        "gate_key": gate_key,
        "gate_name": gate_name,
        "status": result.status.value,
        "threshold": _threshold_for_gate(result.name, config),
        "actual": _actual_for_gate(result.name, data),
        "reason": result.reason,
        "source": "pipeline",
    }
    if result.status == GateStatus.WARNING and result.deduction:
        payload["deduction"] = result.deduction
    return payload


def build_pipeline_gate_report(
    pipeline_result: PipelineResult,
    *,
    data: dict[str, Any],
    config: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Build gate report entries for all evaluated pipeline gates."""
    return [
        pipeline_gate_result_to_dict(result, data=data, config=config)
        for result in pipeline_result.gate_results
    ]
