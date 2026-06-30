"""Master score grade and interpretation for Scoring Engine v1.0 (Frozen)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScoreGrade:
    code: str
    stars: str
    min_score: float
    max_score: float


GRADE_TABLE: tuple[ScoreGrade, ...] = (
    ScoreGrade("SSS", "★★★★★", 950.0, 1000.0),
    ScoreGrade("SS", "★★★★★", 900.0, 949.0),
    ScoreGrade("S", "★★★★☆", 850.0, 899.0),
    ScoreGrade("A", "★★★★☆", 800.0, 849.0),
    ScoreGrade("B", "★★★☆☆", 750.0, 799.0),
    ScoreGrade("C", "★★☆☆☆", 700.0, 749.0),
    ScoreGrade("D", "★☆☆☆☆", 650.0, 699.0),
    ScoreGrade("F", "Not Recommended", 0.0, 649.0),
)

INTERPRETATION_TABLE: tuple[tuple[float, str], ...] = (
    (950.0, "Exceptional Opportunity"),
    (900.0, "Excellent Opportunity"),
    (850.0, "Strong Opportunity"),
    (800.0, "Good Opportunity"),
    (750.0, "Average Opportunity"),
    (700.0, "Weak Opportunity"),
    (0.0, "Reject"),
)


def grade_from_score(total_score: float) -> ScoreGrade:
    for grade in GRADE_TABLE:
        if grade.min_score <= total_score <= grade.max_score:
            return grade
    return GRADE_TABLE[-1]


def interpretation_from_score(total_score: float) -> str:
    for threshold, label in INTERPRETATION_TABLE:
        if total_score >= threshold:
            return label
    return INTERPRETATION_TABLE[-1][1]
