"""Unit tests for Recommendation Engine v1.0."""

from __future__ import annotations

from dataclasses import replace

from engine.confidence import ConfidenceEngineInput, compute_confidence
from engine.core.types import (
    AgreementReport,
    ConfidenceBreakdown,
    ConfidenceResult,
    ConsistencyReport,
    DomainScore,
    MasterScoreResult,
    ProbabilityResult,
    RiskComponentScore,
    RiskResult,
    RuleResult,
    TrendEngineResult,
    TrendGrade,
    TrendState,
)
from engine.probability import compute_probability
from engine.recommendation import (
    RecommendationEngineInput,
    compute_recommendations,
    evaluate_recommendation,
    load_recommendation_config,
)
from engine.recommendation.grades import resolve_grade
from engine.recommendation.recommendation_engine import RecommendationEngineConfigWrapper
from engine.risk.mapping import decision_from_score, grade_from_score, level_from_score


def _master(score: float, mvp: bool = False) -> MasterScoreResult:
    return MasterScoreResult(
        total_score=score,
        max_score=200.0 if mvp else 1000.0,
        mvp_mode=mvp,
        domains={
            "trend": DomainScore(score=min(score, 200), max_score=200, grade="A", state="Up"),
        },
        grade="A",
    )


def _trend(
    *,
    pass_all: bool = True,
    conflict: bool = False,
    composite_fail: bool = False,
) -> TrendEngineResult:
    if conflict:
        atomic = {
            "TR0001": RuleResult("TR0001", "PASS", 80),
            "TR0002": RuleResult("TR0002", "PASS", 80),
            "TR0003": RuleResult("TR0003", "FAIL", 20),
            "TR0004": RuleResult("TR0004", "FAIL", 20),
        }
    elif pass_all:
        atomic = {
            "TR0001": RuleResult("TR0001", "PASS", 80),
            "TR0002": RuleResult("TR0002", "PASS", 80),
            "TR0003": RuleResult("TR0003", "PASS", 80),
            "TR0004": RuleResult("TR0004", "PASS", 80),
        }
    else:
        atomic = {
            "TR0001": RuleResult("TR0001", "PARTIAL", 50),
            "TR0002": RuleResult("TR0002", "PARTIAL", 50),
            "TR0003": RuleResult("TR0003", "PARTIAL", 50),
            "TR0004": RuleResult("TR0004", "PARTIAL", 50),
        }

    verdict = "FAIL" if composite_fail else ("PASS" if pass_all else "PARTIAL")
    composites = {
        "CTR001": RuleResult("CTR001", verdict, 0, reasons=["Trend Direction"]),
        "CTR002": RuleResult("CTR002", verdict, 0, reasons=["Trend Strength"]),
        "CTR003": RuleResult("CTR003", verdict, 0),
        "CTR004": RuleResult("CTR004", verdict, 0),
    }
    return TrendEngineResult(
        trend_score=160.0,
        trend_grade=TrendGrade.A,
        trend_state=TrendState.UP,
        trend_confidence=80.0,
        trend_risk=15.0,
        atomic_results=atomic,
        composite_results=composites,
    )


def _probability(score: float) -> ProbabilityResult:
    return compute_probability(_master(score, mvp=False))


def _confidence(master: MasterScoreResult, probability: ProbabilityResult, trend: TrendEngineResult) -> ConfidenceResult:
    return compute_confidence(
        ConfidenceEngineInput(master=master, probability=probability, trend=trend)
    )


def _risk(score: float) -> RiskResult:
    grade = grade_from_score(score)
    level = level_from_score(score)
    decision = decision_from_score(score)
    return RiskResult(
        risk_score=score,
        risk_grade=grade,
        risk_grade_stars="★" * 5,
        risk_level=level,
        risk_decision=decision,
        components=[
            RiskComponentScore("volatility_risk", "Volatility Risk", score, 20, score * 0.2)
        ],
        config_version="1.0",
    )


def _high_confidence(master: MasterScoreResult, probability: ProbabilityResult, trend: TrendEngineResult) -> ConfidenceResult:
    base = _confidence(master, probability, trend)
    if base.confidence_score >= 70.0:
        return base
    return ConfidenceResult(
        confidence_score=85.0,
        confidence_grade="Strong",
        confidence_level="Trust",
        confidence_stars="★★★★☆",
        rule_consistency=base.rule_consistency,
        engine_consistency=base.engine_consistency,
        agreement_score=85.0,
        data_quality=base.data_quality,
        timeframe_agreement=base.timeframe_agreement,
        historical_stability=base.historical_stability,
        breakdown=list(base.breakdown),
        agreement_report=replace(base.agreement_report, market_regime_agreement=75.0),
        consistency_report=base.consistency_report,
        master_score=master.total_score,
        probability=probability.winning_probability,
        version=base.version,
        reasons=base.reasons,
    )


def _strict_gates(**overrides) -> RecommendationEngineConfigWrapper:
    base = load_recommendation_config()
    gates = replace(base.gates, **overrides)
    return RecommendationEngineConfigWrapper(config=replace(base, gates=gates))


def _input(
    symbol: str,
    master_score: float,
    risk_score: float = 15.0,
    *,
    pass_all: bool = True,
    conflict: bool = False,
    composite_fail: bool = False,
    data_quality_pass: bool = True,
    volume: float = 1000.0,
) -> RecommendationEngineInput:
    master = _master(master_score)
    trend = _trend(pass_all=pass_all, conflict=conflict, composite_fail=composite_fail)
    probability = _probability(master_score)
    confidence = _high_confidence(master, probability, trend)
    risk = _risk(risk_score)
    return RecommendationEngineInput(
        symbol=symbol,
        name=symbol,
        master=master,
        probability=probability,
        confidence=confidence,
        risk=risk,
        trend=trend,
        data_quality_pass=data_quality_pass,
        volume=volume,
        gate_status="PASS",
    )


def test_config_loads_frozen_v1():
    cfg = load_recommendation_config()
    assert cfg.version == "1.0"
    assert cfg.status == "frozen"
    assert cfg.top_n == 20
    assert cfg.gates.master_score_min == 200


def test_same_inputs_same_output():
    first = evaluate_recommendation(_input("A", 920))
    second = evaluate_recommendation(_input("A", 920))
    assert first.recommendation == second.recommendation
    assert first.recommendation_grade == second.recommendation_grade
    assert first.gate_report == second.gate_report


def test_gate_fail_master_score_rejects():
    wrapper = _strict_gates(master_score_min=700.0)
    result = evaluate_recommendation(_input("LOW", 650), config=wrapper)
    assert result.recommendation == "REJECT"
    assert not result.is_candidate
    assert "Master Score" in result.failed_conditions


def test_gate_fail_probability_rejects():
    wrapper = _strict_gates(probability_min=90.0)
    result = evaluate_recommendation(_input("LOW", 720), config=wrapper)
    assert result.recommendation == "REJECT"
    assert "Probability" in result.failed_conditions


def test_gate_fail_risk_rejects():
    wrapper = _strict_gates(risk_max=30.0)
    result = evaluate_recommendation(_input("RISKY", 920, risk_score=45.0), config=wrapper)
    assert result.recommendation == "REJECT"
    assert "Risk" in result.failed_conditions


def test_gate_fail_data_quality_rejects():
    result = evaluate_recommendation(_input("BAD", 920, data_quality_pass=False))
    assert result.recommendation == "REJECT"
    assert "Data Quality" in result.failed_conditions


def test_gate_fail_critical_conflict_rejects():
    wrapper = _strict_gates(critical_conflict_min_pass=2, critical_conflict_min_fail=2)
    result = evaluate_recommendation(_input("CONFLICT", 920, conflict=True), config=wrapper)
    assert result.recommendation == "REJECT"
    assert "Critical Rule Conflict" in result.failed_conditions


def test_gate_fail_composite_validation_rejects():
    wrapper = _strict_gates(max_composite_failures=0)
    result = evaluate_recommendation(_input("COMP", 920, composite_fail=True), config=wrapper)
    assert result.recommendation == "REJECT"
    assert "Composite Validation" in result.failed_conditions


def test_grade_strong_buy():
    master = _master(460)
    stars, action = resolve_grade(
        master=master,
        probability=_probability(460),
        confidence=96.0,
        risk=8.0,
        config=load_recommendation_config(),
    )
    assert stars == "★★★★★"
    assert action == "STRONG BUY"


def test_grade_buy():
    master = _master(410)
    stars, action = resolve_grade(
        master=master,
        probability=_probability(410),
        confidence=91.0,
        risk=18.0,
        config=load_recommendation_config(),
    )
    assert stars == "★★★★☆"
    assert action == "BUY"


def test_grade_watchlist():
    master = _master(360)
    stars, action = resolve_grade(
        master=master,
        probability=_probability(360),
        confidence=82.0,
        risk=28.0,
        config=load_recommendation_config(),
    )
    assert stars == "★★★☆☆"
    assert action == "WATCHLIST"


def test_grade_hold():
    master = _master(250)
    stars, action = resolve_grade(
        master=master,
        probability=_probability(250),
        confidence=72.0,
        risk=35.0,
        config=load_recommendation_config(),
    )
    assert stars == "★★☆☆☆"
    assert action == "HOLD"


def test_grade_not_recommended():
    master = _master(150)
    stars, action = resolve_grade(
        master=master,
        probability=_probability(150),
        confidence=75.0,
        risk=25.0,
        config=load_recommendation_config(),
    )
    assert stars == "★☆☆☆☆"
    assert action == "NOT RECOMMENDED"


def test_ranking_order():
    inputs = [
        _input("LOW_SCORE", 920, volume=500),
        _input("HIGH_SCORE", 960, volume=100),
        replace(_input("MID_SCORE", 940, volume=300), symbol="MID_SCORE"),
    ]
    results = compute_recommendations(inputs, top_n=3)
    ranked = [r for r in results if r.recommendation_rank is not None]
    assert len(ranked) == 3
    assert ranked[0].symbol == "HIGH_SCORE"
    assert ranked[1].symbol == "MID_SCORE"
    assert ranked[2].symbol == "LOW_SCORE"


def test_top_n_limits_output():
    inputs = [_input(f"S{i}", 900 + i, volume=float(i)) for i in range(5)]
    results = compute_recommendations(inputs, top_n=2)
    ranked = [r for r in results if r.recommendation_rank is not None]
    assert len(ranked) == 2


def test_explainability_fields():
    result = evaluate_recommendation(_input("X", 920))
    assert result.master_score == 920
    assert result.winning_probability > 0
    assert result.confidence_score > 0
    assert result.risk_score >= 0
    assert result.domain_breakdown
    assert result.composite_breakdown
    assert len(result.gate_report) == 8
    assert result.version == "1.0"


def test_recommendation_reasons_generated():
    result = evaluate_recommendation(_input("X", 920))
    assert result.is_candidate
    assert len(result.recommendation_reason) >= 1


def test_not_recommended_excluded_from_top():
    inputs = [
        _input("GOOD", 920),
        _input("WEAK", 150),
    ]
    results = compute_recommendations(inputs, top_n=20)
    ranked = [r for r in results if r.recommendation_rank is not None]
    assert len(ranked) == 1
    assert ranked[0].symbol == "GOOD"
