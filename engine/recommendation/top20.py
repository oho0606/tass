from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd

from engine.confidence import ConfidenceEngineInput, compute_confidence
from engine.core.types import (
    ConfidenceResult,
    GateResult,
    GateStatus,
    MasterScoreResult,
    PickResult,
    ProbabilityResult,
    RecommendationResult,
    RiskResult,
    TrendEngineResult,
    TrendState,
)
from engine.data.universe import UniverseEntry
from engine.data.validator import DataValidationResult
from engine.probability import compute_probability
from engine.recommendation.recommendation_engine import (
    RecommendationEngineInput,
    compute_recommendations,
    gate_report_to_dict,
)
from engine.risk import compute_risk

GATE_BLOCKED_LIMIT = 5


@dataclass
class CandidateResult:
    symbol: str
    name: str
    master: MasterScoreResult
    trend: TrendEngineResult
    gate_status: GateStatus
    probability: ProbabilityResult | None = None
    confidence: ConfidenceResult | None = None
    risk: RiskResult | None = None
    data_quality_pass: bool = True
    volume: float | None = None
    pipeline_gate_report: list[dict[str, Any]] | None = None


@dataclass(frozen=True)
class RankTop20Result:
    """Ranked Today's Picks plus high-scoring gate-blocked candidates."""

    picks: list[PickResult]
    gate_blocked: list[PickResult]


def is_gate_eligible(gate_status: GateStatus) -> bool:
    """Return True when pipeline gate allows inclusion in Today's Picks."""
    return str(gate_status).upper() != "FAIL"


def _domain_payload(domain) -> dict | None:
    if domain is None:
        return None
    payload = {
        "score": domain.score,
        "max": domain.max_score,
        "status": domain.status,
    }
    if domain.grade is not None:
        payload["grade"] = domain.grade
    if domain.state is not None:
        payload["state"] = domain.state
    return payload


def _gate_fail_reason(pipeline_gate_report: list[dict[str, Any]] | None) -> str:
    if not pipeline_gate_report:
        return "Pipeline gate FAIL"
    for report in pipeline_gate_report:
        if report.get("source") == "pipeline" and str(report.get("status", "")).upper() == "FAIL":
            return str(report.get("reason") or report.get("gate_name") or "Pipeline gate FAIL")
    return "Pipeline gate FAIL"


def _recommendation_to_pick(result: RecommendationResult) -> PickResult:
    domains = {key: value for key, value in result.domain_breakdown.items() if value is not None}
    recommendation_reports = [gate_report_to_dict(g) for g in result.gate_report]
    gate_report = recommendation_reports
    if result.pipeline_gate_report:
        gate_report = list(result.pipeline_gate_report) + recommendation_reports

    return PickResult(
        rank=result.recommendation_rank or 0,
        symbol=result.symbol,
        name=result.name,
        total_score=result.master_score,
        max_score=result.max_score or 1000.0,
        domains=domains,
        confidence=result.confidence_score,
        risk=result.risk_score,
        reasons=result.recommendation_reason,
        gate=result.gate or "PASS",
        grade=result.grade,
        probability=result.winning_probability,
        probability_grade=result.probability_grade,
        probability_level=result.probability_level,
        risk_grade=result.risk_grade,
        risk_grade_stars=result.risk_grade_stars,
        risk_level=result.risk_level,
        risk_decision=result.risk_decision,
        risk_breakdown=result.risk_breakdown,
        confidence_grade=result.confidence_grade,
        confidence_level=result.confidence_level,
        confidence_stars=result.confidence_stars,
        recommendation=result.recommendation,
        recommendation_grade=result.recommendation_grade,
        recommendation_reason=result.recommendation_reason,
        passed_conditions=result.passed_conditions,
        failed_conditions=result.failed_conditions,
        gate_report=gate_report,
        composite_breakdown=result.composite_breakdown,
    )


def _candidate_to_engine_input(candidate: CandidateResult) -> RecommendationEngineInput | None:
    prob = candidate.probability or compute_probability(candidate.master)
    conf = candidate.confidence or compute_confidence(
        ConfidenceEngineInput(
            master=candidate.master,
            probability=prob,
            trend=candidate.trend,
        )
    )
    if candidate.risk is None:
        return None
    return RecommendationEngineInput(
        symbol=candidate.symbol,
        name=candidate.name,
        master=candidate.master,
        probability=prob,
        confidence=conf,
        risk=candidate.risk,
        trend=candidate.trend,
        data_quality_pass=candidate.data_quality_pass,
        volume=candidate.volume,
        gate_status=candidate.gate_status,
        pipeline_gate_report=candidate.pipeline_gate_report,
    )


def _blocked_pick_from_candidate(candidate: CandidateResult) -> PickResult:
    domains = {
        key: _domain_payload(domain)
        for key, domain in candidate.master.domains.items()
        if domain is not None
    }
    fail_reason = _gate_fail_reason(candidate.pipeline_gate_report)
    return PickResult(
        rank=0,
        symbol=candidate.symbol,
        name=candidate.name,
        total_score=candidate.master.total_score,
        max_score=candidate.master.max_score,
        domains=domains,
        confidence=candidate.confidence.confidence_score if candidate.confidence else None,
        risk=candidate.risk.risk_score if candidate.risk else None,
        reasons=[fail_reason],
        gate="FAIL",
        grade=candidate.master.grade,
        probability=candidate.probability.winning_probability if candidate.probability else None,
        gate_report=candidate.pipeline_gate_report,
    )


def rank_top20(
    candidates: list[CandidateResult],
    top_n: int = 20,
    *,
    eligible_only: bool = True,
    gate_blocked_limit: int = GATE_BLOCKED_LIMIT,
) -> RankTop20Result:
    """Rank candidates via Recommendation Engine v1.0 and return top picks."""
    pool = candidates
    blocked_candidates: list[CandidateResult] = []
    if eligible_only:
        blocked_candidates = [c for c in candidates if not is_gate_eligible(c.gate_status)]
        pool = [c for c in candidates if is_gate_eligible(c.gate_status)]

    engine_inputs: list[RecommendationEngineInput] = []
    for candidate in pool:
        engine_input = _candidate_to_engine_input(candidate)
        if engine_input is not None:
            engine_inputs.append(engine_input)

    results = compute_recommendations(engine_inputs, top_n=top_n)
    ranked = [r for r in results if r.recommendation_rank is not None]
    picks = [_recommendation_to_pick(result) for result in ranked]

    gate_blocked: list[PickResult] = []
    if eligible_only and gate_blocked_limit > 0 and blocked_candidates:
        blocked_candidates.sort(key=lambda item: item.master.total_score, reverse=True)
        gate_blocked = [
            _blocked_pick_from_candidate(candidate)
            for candidate in blocked_candidates[:gate_blocked_limit]
        ]

    return RankTop20Result(picks=picks, gate_blocked=gate_blocked)


def build_candidate(
    entry: UniverseEntry,
    master: MasterScoreResult,
    trend: TrendEngineResult,
    gate_status: GateStatus,
    probability: ProbabilityResult | None = None,
    confidence: ConfidenceResult | None = None,
    df: pd.DataFrame | None = None,
    gate: GateResult | None = None,
    data_valid: bool = True,
    data_quality: DataValidationResult | None = None,
    risk: RiskResult | None = None,
    pipeline_gate_report: list[dict[str, Any]] | None = None,
) -> CandidateResult:
    prob = probability or compute_probability(master)
    validation = data_quality
    data_quality_pass = validation.valid if validation is not None else data_valid
    favorable_trend = trend.trend_state in (TrendState.UP, TrendState.STRONG_UP)
    conf = confidence or compute_confidence(
        ConfidenceEngineInput(
            master=master,
            probability=prob,
            trend=trend,
            data_quality=validation,
            historical_consistency=0.75 if data_quality_pass else None,
            market_regime_agreement=75.0 if favorable_trend else None,
            volume_agreement=75.0 if favorable_trend else None,
            momentum_agreement=75.0 if favorable_trend else None,
        )
    )
    risk_result = risk
    if risk_result is None and df is not None:
        risk_result = compute_risk(
            df,
            trend,
            master,
            probability=prob,
            gate=gate,
            data_valid=data_quality_pass,
        )
    volume = None
    if df is not None and not df.empty and "volume" in df.columns:
        volume = float(df["volume"].iloc[-1])
    return CandidateResult(
        symbol=entry.symbol,
        name=entry.name,
        master=master,
        trend=trend,
        gate_status=gate_status,
        probability=prob,
        confidence=conf,
        risk=risk_result,
        data_quality_pass=data_quality_pass,
        volume=volume,
        pipeline_gate_report=pipeline_gate_report,
    )
