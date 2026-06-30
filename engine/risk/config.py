"""Configuration loader for Risk Engine v1.0."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from engine.risk.mapping import DEFAULT_COMPONENT_WEIGHTS, ComponentWeight


@dataclass(frozen=True)
class RiskThresholds:
    volatility_atr_pct_low: float = 1.0
    volatility_atr_pct_high: float = 5.0
    gap_pct_low: float = 0.5
    gap_pct_high: float = 4.0
    liquidity_value_low: float = 100_000_000.0
    liquidity_value_high: float = 2_000_000_000.0
    trend_score_max: float = 200.0
    rsi_neutral_low: float = 30.0
    rsi_neutral_high: float = 70.0
    ma_extension_low: float = 0.0
    ma_extension_high: float = 10.0
    drawdown_low: float = 0.0
    drawdown_high: float = 20.0
    min_bars: int = 60


@dataclass(frozen=True)
class RiskEngineConfigData:
    version: str = "1.0"
    status: str = "frozen"
    component_weights: tuple[ComponentWeight, ...] = DEFAULT_COMPONENT_WEIGHTS
    thresholds: RiskThresholds = field(default_factory=RiskThresholds)


def _parse_component_weights(raw: list[dict] | None) -> tuple[ComponentWeight, ...]:
    if not raw:
        return DEFAULT_COMPONENT_WEIGHTS
    return tuple(
        ComponentWeight(
            key=str(item["key"]),
            label=str(item["label"]),
            weight=int(item["weight"]),
        )
        for item in raw
    )


def load_risk_config(path: Path | None = None) -> RiskEngineConfigData:
    if path is None:
        path = Path("config/risk_v1.yaml")
    if not path.exists():
        return RiskEngineConfigData()

    with path.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    thresholds_raw = raw.get("thresholds") or {}
    thresholds = RiskThresholds(
        volatility_atr_pct_low=float(thresholds_raw.get("volatility_atr_pct_low", 1.0)),
        volatility_atr_pct_high=float(thresholds_raw.get("volatility_atr_pct_high", 5.0)),
        gap_pct_low=float(thresholds_raw.get("gap_pct_low", 0.5)),
        gap_pct_high=float(thresholds_raw.get("gap_pct_high", 4.0)),
        liquidity_value_low=float(thresholds_raw.get("liquidity_value_low", 100_000_000.0)),
        liquidity_value_high=float(thresholds_raw.get("liquidity_value_high", 2_000_000_000.0)),
        trend_score_max=float(thresholds_raw.get("trend_score_max", 200.0)),
        rsi_neutral_low=float(thresholds_raw.get("rsi_neutral_low", 30.0)),
        rsi_neutral_high=float(thresholds_raw.get("rsi_neutral_high", 70.0)),
        ma_extension_low=float(thresholds_raw.get("ma_extension_low", 0.0)),
        ma_extension_high=float(thresholds_raw.get("ma_extension_high", 10.0)),
        drawdown_low=float(thresholds_raw.get("drawdown_low", 0.0)),
        drawdown_high=float(thresholds_raw.get("drawdown_high", 20.0)),
        min_bars=int(thresholds_raw.get("min_bars", 60)),
    )

    return RiskEngineConfigData(
        version=str(raw.get("version", "1.0")),
        status=str(raw.get("status", "frozen")),
        component_weights=_parse_component_weights(raw.get("component_weights")),
        thresholds=thresholds,
    )
