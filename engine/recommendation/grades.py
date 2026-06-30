"""Grade and action mapping for Recommendation Engine v1.0."""

from __future__ import annotations

from engine.core.types import MasterScoreResult, ProbabilityResult, RecommendationAction
from engine.recommendation.config import GradeThreshold, RecommendationEngineConfig
from engine.recommendation.normalize import normalized_master_score, normalized_probability


def _meets_grade(
    grade: GradeThreshold,
    *,
    master_score: float,
    probability: float,
    confidence: float,
    risk: float,
) -> bool:
    if grade.master_score_min is not None and master_score < grade.master_score_min:
        return False
    if grade.probability_min is not None and probability < grade.probability_min:
        return False
    if grade.confidence_min is not None and confidence < grade.confidence_min:
        return False
    if grade.risk_max is not None and risk > grade.risk_max:
        return False
    return True


def resolve_grade(
    *,
    master: MasterScoreResult,
    probability: ProbabilityResult,
    confidence: float,
    risk: float,
    config: RecommendationEngineConfig,
) -> tuple[str, RecommendationAction]:
    master_score = normalized_master_score(master)
    effective_probability = normalized_probability(master, probability)

    for grade in config.grades:
        if grade.master_score_min is None:
            return grade.stars, grade.action  # type: ignore[return-value]
        if _meets_grade(
            grade,
            master_score=master_score,
            probability=effective_probability,
            confidence=confidence,
            risk=risk,
        ):
            return grade.stars, grade.action  # type: ignore[return-value]
    fallback = config.grades[-1]
    return fallback.stars, fallback.action  # type: ignore[return-value]


def is_recommendable(action: str, config: RecommendationEngineConfig) -> bool:
    return action in config.recommendable_actions
