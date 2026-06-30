"""Pipeline settings loader for Application layer."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from engine.data.engine import DataEngineConfig
from engine.gate.config import GateConfig


@dataclass(frozen=True)
class PipelineSettings:
    """Runtime pipeline configuration from ``config/settings.yaml``."""

    adapter: str = "yahoo"
    min_bars: int = 60
    min_traded_value_ma20: float = 500_000_000.0
    trend_floor_score: float = 120.0
    lookback_days: int = 400
    top_n: int = 20
    cache_dir: Path = Path("data/cache")
    output_dir: Path = Path("output")
    mvp_mode: bool = True

    def to_data_engine_config(self) -> DataEngineConfig:
        """Build data engine configuration."""
        return DataEngineConfig(
            adapter_name=self.adapter,
            min_bars=self.min_bars,
            cache_dir=self.cache_dir,
        )

    def to_gate_config(self) -> GateConfig:
        """Build gate engine configuration."""
        return GateConfig(
            min_bars=self.min_bars,
            min_traded_value_ma20=self.min_traded_value_ma20,
            trend_floor_score=self.trend_floor_score,
        )


def load_pipeline_settings(path: Path | None = None) -> PipelineSettings:
    """Load pipeline settings from YAML.

    Args:
        path: Settings file path; defaults to ``config/settings.yaml``.

    Returns:
        Parsed ``PipelineSettings``.

    Example:
        >>> settings = load_pipeline_settings()
        >>> settings.top_n
        20
    """
    if path is None:
        path = Path("config/settings.yaml")
    if not path.exists():
        return PipelineSettings()

    with path.open(encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}

    return PipelineSettings(
        adapter=str(raw.get("adapter", "yahoo")),
        min_bars=int(raw.get("min_bars", 60)),
        min_traded_value_ma20=float(raw.get("min_traded_value_ma20", 500_000_000)),
        trend_floor_score=float(raw.get("trend_floor_score", 120)),
        lookback_days=int(raw.get("lookback_days", 400)),
        top_n=int(raw.get("top_n", 20)),
        cache_dir=Path(raw.get("cache_dir", "data/cache")),
        output_dir=Path(raw.get("output_dir", "output")),
        mvp_mode=bool(raw.get("mvp_mode", True)),
    )
