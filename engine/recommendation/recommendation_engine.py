"""Recommendation Engine v1.0 — final investment decision layer (Frozen).

Recommendation Engine does not perform new calculations.
It consumes Master Score, Probability, Confidence, and Risk outputs only.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from engine.core.types import (
    ConfidenceResult,
    GateStatus,
    MasterScoreResult,
    ProbabilityResult,
    RecommendationGateReport,
    RecommendationResult,
    RiskResult,
    TrendEngineResult,
)
from engine.recommendation.config import RecommendationEngineConfig, load_recommendation_config
from engine.recommendation.gates import evaluate_recommendation_gates
from engine.recommendation.grades import is_recommendable, resolve_grade
from engine.recommendation.reasons import build_composite_breakdown, generate_recommendation_reasons


@dataclass
class RecommendationEngineInput:
    symbol: str
    name: str
    master: MasterScoreResult
    probability: ProbabilityResult
    confidence: ConfidenceResult
    risk: RiskResult
    trend: TrendEngineResult
    data_quality_pass: bool = True
    market_regime_pass: bool | None = None
    volume: float | None = None
    gate_status: GateStatus | None = None
    pipeline_gate_report: list[dict[str, Any]] | None = None


@dataclass
class RecommendationEngineConfigWrapper:
    config: RecommendationEngineConfig | None = None
    config_path: Path | None = None


def _resolve_config(
    wrapper: RecommendationEngineConfigWrapper | None,
) -> RecommendationEngineConfig:
    if wrapper and wrapper.config:
        return wrapper.config
    if wrapper and wrapper.config_path:
        return load_recommendation_config(wrapper.config_path)
    return load_recommendation_config()


def _domain_breakdown(master: MasterScoreResult) -> dict[str, Any]:
    breakdown: dict[str, Any] = {}
    for key, domain in master.domains.items():
        if domain is None:
            breakdown[key] = None
            continue
        payload: dict[str, Any] = {
            "score": domain.score,
            "max": domain.max_score,
            "status": domain.status,
        }
        if domain.grade is not None:
            payload["grade"] = domain.grade
        if domain.state is not None:
            payload["state"] = domain.state
        breakdown[key] = payload
    return breakdown


def _risk_breakdown_payload(risk: RiskResult) -> list[dict[str, Any]]:
    return [
        {
            "key": c.key,
            "label": c.label,
            "score": c.score,
            "weight": c.weight,
            "contribution": c.contribution,
            "reasons": c.reasons,
        }
        for c in risk.components
    ]


def _ranking_key(item: RecommendationResult) -> tuple:
    return (
        item.master_score,
        item.winning_probability,
        item.confidence_score,
        -item.risk_score,
        item.volume or 0.0,
    )


def evaluate_recommendation(
    engine_input: RecommendationEngineInput,
    *,
    config: RecommendationEngineConfigWrapper | None = None,
) -> RecommendationResult:
    """Evaluate a single symbol for recommendation gates, grade, and action."""
    cfg = _resolve_config(config)
    master = engine_input.master
    probability = engine_input.probability
    confidence = engine_input.confidence
    risk = engine_input.risk
    trend = engine_input.trend

    all_pass, gate_report, passed, failed = evaluate_recommendation_gates(
        master=master,
        probability=probability,
        confidence=confidence,
        risk=risk,
        trend=trend,
        data_quality_pass=engine_input.data_quality_pass,
        market_regime_pass=engine_input.market_regime_pass,
        thresholds=cfg.gates,
    )

    if not all_pass:
        return RecommendationResult(
            symbol=engine_input.symbol,
            name=engine_input.name,
            recommendation="REJECT",
            recommendation_grade="—",
            recommendation_rank=None,
            master_score=master.total_score,
            winning_probability=probability.winning_probability,
            confidence_score=confidence.confidence_score,
            risk_score=risk.risk_score,
            recommendation_reason=[],
            domain_breakdown=_domain_breakdown(master),
            composite_breakdown=build_composite_breakdown(trend),
            gate_report=gate_report,
            passed_conditions=passed,
            failed_conditions=failed,
            is_candidate=False,
            version=cfg.version,
            volume=engine_input.volume,
            max_score=master.max_score,
            grade=master.grade,
            probability_grade=probability.probability_grade,
            probability_level=probability.probability_level,
            confidence_grade=confidence.confidence_grade,
            confidence_level=confidence.confidence_level,
            confidence_stars=confidence.confidence_stars,
            risk_grade=risk.risk_grade,
            risk_grade_stars=risk.risk_grade_stars,
            risk_level=risk.risk_level,
            risk_decision=risk.risk_decision,
            risk_breakdown=_risk_breakdown_payload(risk),
            gate=engine_input.gate_status,
            pipeline_gate_report=engine_input.pipeline_gate_report,
        )

    stars, action = resolve_grade(
        master=master,
        probability=probability,
        confidence=confidence.confidence_score,
        risk=risk.risk_score,
        config=cfg,
    )

    reasons = generate_recommendation_reasons(trend, confidence, risk)

    return RecommendationResult(
        symbol=engine_input.symbol,
        name=engine_input.name,
        recommendation=action,
        recommendation_grade=stars,
        recommendation_rank=None,
        master_score=master.total_score,
        winning_probability=probability.winning_probability,
        confidence_score=confidence.confidence_score,
        risk_score=risk.risk_score,
        recommendation_reason=reasons,
        domain_breakdown=_domain_breakdown(master),
        composite_breakdown=build_composite_breakdown(trend),
        gate_report=gate_report,
        passed_conditions=passed,
        failed_conditions=failed,
        is_candidate=True,
        version=cfg.version,
        volume=engine_input.volume,
        max_score=master.max_score,
        grade=master.grade,
        probability_grade=probability.probability_grade,
        probability_level=probability.probability_level,
        confidence_grade=confidence.confidence_grade,
        confidence_level=confidence.confidence_level,
        confidence_stars=confidence.confidence_stars,
        risk_grade=risk.risk_grade,
        risk_grade_stars=risk.risk_grade_stars,
        risk_level=risk.risk_level,
        risk_decision=risk.risk_decision,
        risk_breakdown=_risk_breakdown_payload(risk),
        gate=engine_input.gate_status,
        pipeline_gate_report=engine_input.pipeline_gate_report,
    )


def compute_recommendations(
    inputs: list[RecommendationEngineInput],
    *,
    top_n: int | None = None,
    config: RecommendationEngineConfigWrapper | None = None,
) -> list[RecommendationResult]:
    """Evaluate all symbols, rank candidates, and return top recommendations."""
    cfg = _resolve_config(config)
    limit = top_n if top_n is not None else cfg.top_n

    evaluated = [evaluate_recommendation(item, config=config) for item in inputs]
    candidates = [
        r for r in evaluated if r.is_candidate and is_recommendable(r.recommendation, cfg)
    ]
    candidates.sort(key=_ranking_key, reverse=True)

    ranked: list[RecommendationResult] = []
    for rank, result in enumerate(candidates[:limit], start=1):
        ranked.append(
            RecommendationResult(
                symbol=result.symbol,
                name=result.name,
                recommendation=result.recommendation,
                recommendation_grade=result.recommendation_grade,
                recommendation_rank=rank,
                master_score=result.master_score,
                winning_probability=result.winning_probability,
                confidence_score=result.confidence_score,
                risk_score=result.risk_score,
                recommendation_reason=result.recommendation_reason,
                domain_breakdown=result.domain_breakdown,
                composite_breakdown=result.composite_breakdown,
                gate_report=result.gate_report,
                passed_conditions=result.passed_conditions,
                failed_conditions=result.failed_conditions,
                is_candidate=True,
                version=result.version,
                volume=result.volume,
                max_score=result.max_score,
                grade=result.grade,
                probability_grade=result.probability_grade,
                probability_level=result.probability_level,
                confidence_grade=result.confidence_grade,
                confidence_level=result.confidence_level,
                confidence_stars=result.confidence_stars,
                risk_grade=result.risk_grade,
                risk_grade_stars=result.risk_grade_stars,
                risk_level=result.risk_level,
                risk_decision=result.risk_decision,
                risk_breakdown=result.risk_breakdown,
                gate=result.gate,
                pipeline_gate_report=result.pipeline_gate_report,
            )
        )

    rejected = [r for r in evaluated if r not in candidates]
    return ranked + rejected


def gate_report_to_dict(report: RecommendationGateReport) -> dict[str, str]:
    return {
        "gate_key": report.gate_key,
        "gate_name": report.gate_name,
        "status": report.status,
        "threshold": report.threshold,
        "actual": report.actual,
        "reason": report.reason,
    }
