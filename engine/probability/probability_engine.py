"""Probability Engine v1.0 — maps Master Score to calibrated Winning Probability."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from engine.core.types import ConfidenceInterval, MasterScoreResult, ProbabilityResult
from engine.probability.calibration import CalibrationConfig, load_calibration_config
from engine.probability.mapping import (
    find_bucket,
    interpolate_probability,
    level_from_probability,
)


@dataclass
class ProbabilityEngineConfig:
    calibration: CalibrationConfig | None = None
    calibration_path: Path | None = None


def _resolve_calibration(config: ProbabilityEngineConfig | None) -> CalibrationConfig:
    if config and config.calibration:
        return config.calibration
    if config and config.calibration_path:
        return load_calibration_config(config.calibration_path)
    return load_calibration_config()


def compute_probability(
    master: MasterScoreResult | float,
    config: ProbabilityEngineConfig | None = None,
) -> ProbabilityResult:
    """Convert Master Score to a calibrated Winning Probability.

    Probability Engine does not score, predict, or recommend.
    Same Master Score always yields the same Probability (deterministic).
    """
    calibration = _resolve_calibration(config)
    master_score = master.total_score if isinstance(master, MasterScoreResult) else float(master)
    clamped_score = max(0.0, min(master_score, 1000.0))

    bucket = find_bucket(clamped_score, calibration.buckets)
    probability = interpolate_probability(clamped_score, bucket)
    level = level_from_probability(probability)

    ci = ConfidenceInterval(
        lower=max(0.0, probability - bucket.confidence_margin),
        upper=min(100.0, probability + bucket.confidence_margin),
    )

    reasons = [
        f"Master Score {clamped_score:.1f} → bucket [{bucket.min_score:.0f}–{bucket.max_score:.0f}]",
        f"Historical win rate {bucket.historical_win_rate:.1f}% (n={bucket.sample_size})",
        f"Calibrated probability {probability:.2f}% ({level.label})",
        f"Calibration v{calibration.version} ({calibration.last_calibration_date})",
    ]

    return ProbabilityResult(
        master_score=clamped_score,
        winning_probability=round(probability, 2),
        probability_grade=level.label,
        probability_level=level.stars,
        calibration_version=calibration.version,
        historical_win_rate=bucket.historical_win_rate,
        sample_size=bucket.sample_size,
        confidence_interval=ci,
        last_calibration_date=calibration.last_calibration_date,
        score_bucket_min=bucket.min_score,
        score_bucket_max=bucket.max_score,
        reasons=reasons,
    )
