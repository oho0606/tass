from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

DEFAULT_GATE_PIPELINE_PATH = Path("config/gate_pipeline_v1.yaml")


@dataclass
class GateConfig:
    min_bars: int = 60
    min_traded_value_ma20: float = 500_000_000
    trend_floor_score: float = 120.0


def load_gate_pipeline_yaml(path: Path | None = None) -> dict[str, Any]:
    """Load gate pipeline YAML configuration."""
    config_path = path or DEFAULT_GATE_PIPELINE_PATH
    if not config_path.exists():
        return {}

    with config_path.open(encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}

    return raw.get("gates") or raw


def merge_gate_config(
    pipeline_gates: dict[str, Any] | None,
    gate_cfg: GateConfig,
) -> dict[str, dict[str, Any]]:
    """Merge YAML gate settings with runtime ``GateConfig`` from settings.yaml."""
    gates = pipeline_gates or {}

    config: dict[str, dict[str, Any]] = {}
    for key in ("data_quality", "market", "liquidity", "trend", "volatility"):
        config[key] = dict(gates.get(key) or {})

    config["data_quality"]["min_bars"] = gate_cfg.min_bars
    config["liquidity"]["min_traded_value_ma20"] = gate_cfg.min_traded_value_ma20
    config["trend"]["floor_score"] = gate_cfg.trend_floor_score
    return config
