"""Calibration configuration loader for Probability Engine v1.0."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from engine.probability.mapping import DEFAULT_SCORE_BUCKETS, ScoreBucket


@dataclass(frozen=True)
class CalibrationConfig:
    version: str = "1.0"
    status: str = "frozen"
    last_calibration_date: str = "2026-01-01"
    calibration_sources: tuple[str, ...] = (
        "historical_backtest",
        "walk_forward_test",
        "paper_trading",
        "live_trading",
        "monte_carlo_simulation",
    )
    buckets: tuple[ScoreBucket, ...] = DEFAULT_SCORE_BUCKETS


def _parse_bucket(raw: dict) -> ScoreBucket:
    return ScoreBucket(
        min_score=float(raw["min_score"]),
        max_score=float(raw["max_score"]),
        prob_min=float(raw["prob_min"]),
        prob_max=float(raw["prob_max"]),
        historical_win_rate=float(raw["historical_win_rate"]),
        sample_size=int(raw["sample_size"]),
        confidence_margin=float(raw["confidence_margin"]),
    )


def load_calibration_config(path: Path | None = None) -> CalibrationConfig:
    if path is None:
        path = Path("config/probability_v1.yaml")
    if not path.exists():
        return CalibrationConfig()

    with path.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    buckets_raw = raw.get("buckets")
    buckets = (
        tuple(_parse_bucket(item) for item in buckets_raw) if buckets_raw else DEFAULT_SCORE_BUCKETS
    )

    sources = raw.get("calibration_sources")
    return CalibrationConfig(
        version=str(raw.get("version", "1.0")),
        status=str(raw.get("status", "frozen")),
        last_calibration_date=str(raw.get("last_calibration_date", "2026-01-01")),
        calibration_sources=tuple(sources) if sources else CalibrationConfig().calibration_sources,
        buckets=buckets,
    )
