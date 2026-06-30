"""Configuration loader for Confidence Engine v1.0."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

DEFAULT_COMPONENT_WEIGHTS: dict[str, float] = {
    "rule_consistency": 20.0,
    "engine_consistency": 20.0,
    "indicator_agreement": 10.0,
    "composite_agreement": 10.0,
    "trend_agreement": 10.0,
    "volume_agreement": 5.0,
    "momentum_agreement": 5.0,
    "volatility_agreement": 5.0,
    "multi_timeframe": 5.0,
    "market_regime": 5.0,
    "data_quality": 3.0,
    "signal_stability": 1.0,
    "historical_consistency": 1.0,
}


@dataclass(frozen=True)
class ConfidenceEngineConfig:
    version: str = "1.0"
    status: str = "frozen"
    component_weights: dict[str, float] | None = None
    pending_domain_ratio: float = 0.5
    default_historical_consistency: float = 0.5


def load_confidence_config(path: Path | None = None) -> ConfidenceEngineConfig:
    if path is None:
        path = Path("config/confidence_v1.yaml")
    if not path.exists():
        return ConfidenceEngineConfig()

    with path.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    weights_raw = raw.get("component_weights")
    weights = {str(k): float(v) for k, v in weights_raw.items()} if weights_raw else None

    return ConfidenceEngineConfig(
        version=str(raw.get("version", "1.0")),
        status=str(raw.get("status", "frozen")),
        component_weights=weights,
        pending_domain_ratio=float(raw.get("pending_domain_ratio", 0.5)),
        default_historical_consistency=float(raw.get("default_historical_consistency", 0.5)),
    )
