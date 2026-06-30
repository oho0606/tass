"""Grade and level mapping for Confidence Engine v1.0 (Frozen)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ConfidenceGrade:
    label: str
    stars: str
    min_score: float


@dataclass(frozen=True)
class ConfidenceLevel:
    label: str
    min_score: float


CONFIDENCE_GRADES: tuple[ConfidenceGrade, ...] = (
    ConfidenceGrade("Exceptional", "★★★★★", 95.0),
    ConfidenceGrade("Excellent", "★★★★★", 90.0),
    ConfidenceGrade("Strong", "★★★★☆", 80.0),
    ConfidenceGrade("Good", "★★★★☆", 70.0),
    ConfidenceGrade("Average", "★★★☆☆", 60.0),
    ConfidenceGrade("Weak", "★★☆☆☆", 50.0),
    ConfidenceGrade("Low", "★☆☆☆☆", 0.0),
)

CONFIDENCE_LEVELS: tuple[ConfidenceLevel, ...] = (
    ConfidenceLevel("Very High Confidence", 95.0),
    ConfidenceLevel("High Confidence", 90.0),
    ConfidenceLevel("Reliable", 80.0),
    ConfidenceLevel("Acceptable", 70.0),
    ConfidenceLevel("Caution", 60.0),
    ConfidenceLevel("Do Not Trust", 0.0),
)


def grade_from_score(score: float) -> ConfidenceGrade:
    clamped = max(0.0, min(score, 100.0))
    for grade in CONFIDENCE_GRADES:
        if clamped >= grade.min_score:
            return grade
    return CONFIDENCE_GRADES[-1]


def level_from_score(score: float) -> ConfidenceLevel:
    clamped = max(0.0, min(score, 100.0))
    for level in CONFIDENCE_LEVELS:
        if clamped >= level.min_score:
            return level
    return CONFIDENCE_LEVELS[-1]
