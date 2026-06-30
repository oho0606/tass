"""Unit tests for Confidence Engine v1.0."""

from __future__ import annotations

import pandas as pd

from engine.confidence import ConfidenceEngineInput, compute_confidence
from engine.confidence.config import ConfidenceEngineConfig
from engine.confidence.grades import grade_from_score, level_from_score
from engine.core.types import MasterScoreResult, RuleResult, TrendEngineResult, TrendGrade, TrendState
from engine.data.validator import DataValidationResult
from engine.domains.trend_engine import evaluate_trend_engine
from engine.indicators.registry import compute_all
from engine.probability import compute_probability
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def _master(score: float = 180.0, mvp_mode: bool = True) -> MasterScoreResult:
    return MasterScoreResult(
        total_score=score,
        max_score=1000.0 if not mvp_mode else 200.0,
        mvp_mode=mvp_mode,
        domains={"trend": None},
    )


def _aligned_atomics() -> dict[str, RuleResult]:
    return {
        "TR0001": RuleResult("TR0001", "PASS", 18.0, confidence_delta=3.0),
        "TR0002": RuleResult("TR0002", "PASS", 17.0, confidence_delta=3.0),
        "TR0003": RuleResult("TR0003", "FAIL", 2.0, confidence_delta=1.0),
        "TR0004": RuleResult("TR0004", "FAIL", 1.0, confidence_delta=1.0),
    }


def _aligned_composites() -> dict[str, RuleResult]:
    return {
        "CTR001": RuleResult("CTR001", "PASS", 0.0, metadata={"direction": "Up"}),
        "CTR002": RuleResult("CTR002", "PASS", 0.0),
        "CTR003": RuleResult("CTR003", "PASS", 0.0),
        "CTR004": RuleResult("CTR004", "PARTIAL", 0.0),
        "CTR005": RuleResult("CTR005", "PASS", 0.0),
        "CTR006": RuleResult("CTR006", "PASS", 0.0),
        "CTR007": RuleResult("CTR007", "PARTIAL", 0.0),
        "CTR008": RuleResult("CTR008", "PASS", 0.0),
        "CTR009": RuleResult("CTR009", "PASS", 0.0),
        "CTR010": RuleResult("CTR010", "PASS", 0.0),
    }


def _trend(atomics: dict[str, RuleResult], composites: dict[str, RuleResult]) -> TrendEngineResult:
    return TrendEngineResult(
        trend_score=185.0,
        trend_grade=TrendGrade.S,
        trend_state=TrendState.STRONG_UP,
        trend_confidence=72.0,
        trend_risk=25.0,
        atomic_results=atomics,
        composite_results=composites,
    )


def test_same_inputs_same_confidence():
    atomics = _aligned_atomics()
    composites = _aligned_composites()
    master = _master()
    trend = _trend(atomics, composites)
    first = compute_confidence(ConfidenceEngineInput(master=master, trend=trend))
    second = compute_confidence(ConfidenceEngineInput(master=master, trend=trend))
    assert first == second


def test_confidence_range_0_to_100():
    atomics = _aligned_atomics()
    composites = _aligned_composites()
    result = compute_confidence(
        ConfidenceEngineInput(master=_master(), trend=_trend(atomics, composites))
    )
    assert 0.0 <= result.confidence_score <= 100.0


def test_aligned_signals_high_confidence():
    atomics = _aligned_atomics()
    composites = _aligned_composites()
    result = compute_confidence(
        ConfidenceEngineInput(master=_master(), trend=_trend(atomics, composites))
    )
    assert result.confidence_score >= 70.0
    assert result.rule_consistency >= 15.0
    assert result.agreement_score >= 25.0


def test_conflicting_signals_lower_confidence():
    atomics = {
        "TR0001": RuleResult("TR0001", "PASS", 18.0),
        "TR0002": RuleResult("TR0002", "FAIL", 2.0),
        "TR0003": RuleResult("TR0003", "PASS", 16.0),
        "TR0004": RuleResult("TR0004", "PASS", 15.0),
    }
    composites = {
        "CTR001": RuleResult("CTR001", "PARTIAL", 0.0, metadata={"direction": "Mixed"}),
        "CTR002": RuleResult("CTR002", "FAIL", 0.0),
        "CTR003": RuleResult("CTR003", "FAIL", 0.0),
        "CTR004": RuleResult("CTR004", "FAIL", 0.0),
        "CTR005": RuleResult("CTR005", "FAIL", 0.0),
        "CTR006": RuleResult("CTR006", "FAIL", 0.0),
        "CTR007": RuleResult("CTR007", "FAIL", 0.0),
        "CTR008": RuleResult("CTR008", "FAIL", 0.0),
        "CTR009": RuleResult("CTR009", "FAIL", 0.0),
        "CTR010": RuleResult("CTR010", "FAIL", 0.0),
    }
    aligned = compute_confidence(
        ConfidenceEngineInput(master=_master(), trend=_trend(_aligned_atomics(), _aligned_composites()))
    )
    conflicted = compute_confidence(
        ConfidenceEngineInput(
            master=_master(),
            trend=_trend(atomics, composites),
        )
    )
    assert conflicted.confidence_score < aligned.confidence_score


def test_grade_boundaries():
    assert grade_from_score(95.0).label == "Exceptional"
    assert grade_from_score(94.9).label == "Excellent"
    assert grade_from_score(90.0).label == "Excellent"
    assert grade_from_score(89.9).label == "Strong"
    assert grade_from_score(80.0).label == "Strong"
    assert grade_from_score(79.9).label == "Good"
    assert grade_from_score(70.0).label == "Good"
    assert grade_from_score(69.9).label == "Average"
    assert grade_from_score(60.0).label == "Average"
    assert grade_from_score(59.9).label == "Weak"
    assert grade_from_score(50.0).label == "Weak"
    assert grade_from_score(49.9).label == "Low"


def test_level_boundaries():
    assert level_from_score(95.0).label == "Very High Confidence"
    assert level_from_score(94.9).label == "High Confidence"
    assert level_from_score(90.0).label == "High Confidence"
    assert level_from_score(89.9).label == "Reliable"
    assert level_from_score(80.0).label == "Reliable"
    assert level_from_score(79.9).label == "Acceptable"
    assert level_from_score(70.0).label == "Acceptable"
    assert level_from_score(69.9).label == "Caution"
    assert level_from_score(60.0).label == "Caution"
    assert level_from_score(59.9).label == "Do Not Trust"


def test_explainability_fields():
    atomics = _aligned_atomics()
    composites = _aligned_composites()
    master = _master(875.0, mvp_mode=False)
    prob = compute_probability(master)
    result = compute_confidence(
        ConfidenceEngineInput(master=master, probability=prob, trend=_trend(atomics, composites))
    )
    assert result.master_score == 875.0
    assert result.probability == prob.winning_probability
    assert len(result.breakdown) == 13
    assert result.breakdown[0].maximum == 20.0
    assert result.agreement_report.agreement_score > 0
    assert result.consistency_report.rule_consistency > 0
    assert result.confidence_grade
    assert result.confidence_level
    assert result.confidence_stars
    assert len(result.reasons) >= 4


def test_data_quality_invalid_reduces_confidence():
    atomics = _aligned_atomics()
    composites = _aligned_composites()
    valid = compute_confidence(
        ConfidenceEngineInput(
            master=_master(),
            trend=_trend(atomics, composites),
            data_quality=DataValidationResult(valid=True),
        )
    )
    invalid = compute_confidence(
        ConfidenceEngineInput(
            master=_master(),
            trend=_trend(atomics, composites),
            data_quality=DataValidationResult(valid=False, errors=["empty_dataframe"]),
        )
    )
    assert invalid.data_quality == 0.0
    assert invalid.confidence_score < valid.confidence_score


def test_does_not_modify_master_or_probability():
    atomics = _aligned_atomics()
    composites = _aligned_composites()
    master = _master(875.0, mvp_mode=False)
    prob = compute_probability(master)
    original_score = master.total_score
    original_prob = prob.winning_probability
    compute_confidence(ConfidenceEngineInput(master=master, probability=prob, trend=_trend(atomics, composites)))
    assert master.total_score == original_score
    assert prob.winning_probability == original_prob


def test_accepts_master_score_only():
    result = compute_confidence(_master())
    assert 0.0 <= result.confidence_score <= 100.0


def test_uptrend_pipeline_confidence():
    df = compute_all(make_uptrend_ohlcv(n=80))
    trend = evaluate_trend_engine(df)
    from engine.scoring.scoring_engine import compute_master_score

    master = compute_master_score(trend, mvp_mode=True)
    result = compute_confidence(ConfidenceEngineInput(master=master, trend=trend))
    assert result.confidence_score >= 60.0


def test_component_weights_sum_to_100():
    config = ConfidenceEngineConfig()
    from engine.confidence.config import DEFAULT_COMPONENT_WEIGHTS

    assert sum(DEFAULT_COMPONENT_WEIGHTS.values()) == 100.0
