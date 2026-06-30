"""Score-to-probability mapping tables for Probability Engine v1.0 (Frozen)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScoreBucket:
    min_score: float
    max_score: float
    prob_min: float
    prob_max: float
    historical_win_rate: float
    sample_size: int
    confidence_margin: float


@dataclass(frozen=True)
class ProbabilityLevel:
    label: str
    stars: str
    min_probability: float


DEFAULT_SCORE_BUCKETS: tuple[ScoreBucket, ...] = (
    ScoreBucket(990, 1000, 95.0, 99.0, 97.0, 142, 1.5),
    ScoreBucket(950, 989, 90.0, 94.0, 92.0, 318, 1.8),
    ScoreBucket(900, 949, 82.0, 89.0, 85.5, 456, 2.0),
    ScoreBucket(850, 899, 74.0, 81.0, 77.5, 512, 2.2),
    ScoreBucket(800, 849, 66.0, 73.0, 69.5, 589, 2.4),
    ScoreBucket(750, 799, 58.0, 65.0, 61.5, 634, 2.6),
    ScoreBucket(700, 749, 50.0, 57.0, 53.5, 701, 2.8),
    ScoreBucket(650, 699, 42.0, 49.0, 45.5, 768, 3.0),
    ScoreBucket(600, 649, 35.0, 41.0, 38.0, 812, 3.2),
    ScoreBucket(0, 599, 5.0, 34.9, 20.0, 1240, 3.5),
)

PROBABILITY_LEVELS: tuple[ProbabilityLevel, ...] = (
    ProbabilityLevel("Exceptional", "★★★★★", 95.0),
    ProbabilityLevel("Excellent", "★★★★★", 90.0),
    ProbabilityLevel("Strong", "★★★★☆", 80.0),
    ProbabilityLevel("Good", "★★★★☆", 70.0),
    ProbabilityLevel("Average", "★★★☆☆", 60.0),
    ProbabilityLevel("Weak", "★★☆☆☆", 50.0),
    ProbabilityLevel("Reject", "★☆☆☆☆", 0.0),
)


def find_bucket(master_score: float, buckets: tuple[ScoreBucket, ...]) -> ScoreBucket:
    clamped = max(0.0, min(master_score, 1000.0))
    for bucket in buckets:
        if bucket.min_score <= clamped <= bucket.max_score:
            return bucket
    return buckets[-1]


def interpolate_probability(master_score: float, bucket: ScoreBucket) -> float:
    clamped = max(bucket.min_score, min(master_score, bucket.max_score))
    span = bucket.max_score - bucket.min_score
    if span <= 0:
        return bucket.prob_min
    ratio = (clamped - bucket.min_score) / span
    return bucket.prob_min + ratio * (bucket.prob_max - bucket.prob_min)


def level_from_probability(probability: float) -> ProbabilityLevel:
    for level in PROBABILITY_LEVELS:
        if probability >= level.min_probability:
            return level
    return PROBABILITY_LEVELS[-1]
