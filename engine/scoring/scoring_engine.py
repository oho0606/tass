"""Scoring Engine v1.0 — aggregates Domain Engine scores into Master Score."""

from __future__ import annotations

from engine.core.types import (
    DomainBundle,
    DomainEngineResult,
    DomainScore,
    EngineBreakdown,
    MasterScoreResult,
    MovingAverageEngineResult,
    TrendEngineResult,
    VolumeEngineResult,
)
from engine.scoring.domain_budgets import (
    DOMAIN_ALIASES,
    ENGINE_WEIGHTS,
    MASTER_MAX_SCORE,
    MVP_ENGINES,
)
from engine.scoring.grades import grade_from_score, interpretation_from_score


def _resolve_engine_key(key: str) -> str:
    return DOMAIN_ALIASES.get(key, key)


def _trend_to_domain(trend: TrendEngineResult) -> DomainScore:
    _, max_score = ENGINE_WEIGHTS["trend"]
    return DomainScore(
        score=trend.trend_score,
        max_score=max_score,
        grade=trend.trend_grade.value,
        state=trend.trend_state.value,
        status="implemented",
    )


def _ma_to_domain(ma: MovingAverageEngineResult) -> DomainScore:
    _, max_score = ENGINE_WEIGHTS["moving_average"]
    return DomainScore(
        score=ma.ma_score,
        max_score=max_score,
        grade=ma.ma_grade,
        state=ma.ma_state,
        status="implemented",
    )


def _volume_to_domain(volume: VolumeEngineResult) -> DomainScore:
    _, max_score = ENGINE_WEIGHTS["volume"]
    return DomainScore(
        score=volume.vl_score,
        max_score=max_score,
        grade=volume.vl_grade,
        state=volume.vl_state,
        status="implemented",
    )


def _generic_to_domain(result: DomainEngineResult) -> DomainScore:
    _, max_score = ENGINE_WEIGHTS[result.engine_key]
    return DomainScore(
        score=result.score,
        max_score=max_score,
        grade=result.grade,
        state=result.state,
        status="implemented",
    )


def _build_breakdown(engine_key: str, domain: DomainScore) -> EngineBreakdown:
    engine_name, weight = ENGINE_WEIGHTS[engine_key]
    maximum = domain.max_score if domain.max_score > 0 else weight
    normalized = domain.score / maximum if maximum > 0 else 0.0
    return EngineBreakdown(
        engine_name=engine_name,
        engine_key=engine_key,
        raw_score=domain.score,
        maximum_score=maximum,
        normalized_score=normalized,
        weight=weight,
        contribution=domain.score,
        final_score=domain.score,
        status=domain.status,
    )


def _pending_domain(engine_key: str) -> DomainScore:
    _, max_score = ENGINE_WEIGHTS[engine_key]
    return DomainScore(score=0.0, max_score=max_score, status="pending")


def _clamp_score(score: float, maximum: float) -> float:
    return max(0.0, min(score, maximum))


def compute_master_score(
    trend: TrendEngineResult | None = None,
    moving_average: MovingAverageEngineResult | None = None,
    volume: VolumeEngineResult | None = None,
    bundle: DomainBundle | None = None,
    domains: dict[str, DomainScore] | None = None,
    mvp_mode: bool = True,
) -> MasterScoreResult:
    """Aggregate domain scores into a deterministic Master Score.

    Scoring Engine does not reference Atomic or Composite Rules directly.
    It only consumes Domain Engine outputs.
    """
    if bundle is not None:
        trend = bundle.trend
        moving_average = bundle.moving_average
        volume = bundle.volume

    active_keys = MVP_ENGINES if mvp_mode else frozenset(ENGINE_WEIGHTS)
    provided: dict[str, DomainScore] = {}

    if trend is not None:
        provided["trend"] = _trend_to_domain(trend)

    if moving_average is not None:
        provided["moving_average"] = _ma_to_domain(moving_average)

    if volume is not None:
        provided["volume"] = _volume_to_domain(volume)

    if bundle is not None:
        for key, result in bundle.domains.items():
            if key in ENGINE_WEIGHTS:
                provided[key] = _generic_to_domain(result)

    if domains:
        for key, domain in domains.items():
            resolved = _resolve_engine_key(key)
            if resolved in ENGINE_WEIGHTS:
                provided[resolved] = domain

    result_domains: dict[str, DomainScore | None] = {}
    breakdown: list[EngineBreakdown] = []
    total = 0.0
    active_max = 0.0
    reasons: list[str] = []

    for engine_key in ENGINE_WEIGHTS:
        if engine_key in active_keys and engine_key in provided:
            domain = provided[engine_key]
            domain.score = _clamp_score(domain.score, domain.max_score)
            result_domains[engine_key] = domain
            breakdown.append(_build_breakdown(engine_key, domain))
            total += domain.score
            active_max += domain.max_score
            if engine_key == "trend" and trend is not None:
                reasons.extend(trend.reasons)
            elif engine_key == "moving_average" and moving_average is not None:
                reasons.extend(moving_average.reasons)
            elif engine_key == "volume" and volume is not None:
                reasons.extend(volume.reasons)
            elif bundle is not None and engine_key in bundle.domains:
                reasons.extend(bundle.domains[engine_key].reasons)
        elif engine_key in active_keys:
            pending = _pending_domain(engine_key)
            result_domains[engine_key] = pending
            breakdown.append(_build_breakdown(engine_key, pending))
        else:
            result_domains[engine_key] = None

    max_score = active_max if mvp_mode else MASTER_MAX_SCORE
    grade = grade_from_score(total)
    interpretation = interpretation_from_score(total)

    return MasterScoreResult(
        total_score=total,
        max_score=max_score,
        mvp_mode=mvp_mode,
        domains=result_domains,
        grade=grade.code,
        grade_stars=grade.stars,
        interpretation=interpretation,
        engine_breakdown=breakdown,
        reasons=reasons,
    )
