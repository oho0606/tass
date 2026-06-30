"""Unit tests for Scoring Engine v1.0."""

from __future__ import annotations

import pytest

from engine.core.types import (
    DomainScore,
    MovingAverageEngineResult,
    TrendEngineResult,
    TrendGrade,
    TrendState,
    VolumeEngineResult,
)
from engine.scoring.domain_budgets import ENGINE_WEIGHTS, MASTER_MAX_SCORE
from engine.scoring.grades import grade_from_score, interpretation_from_score
from engine.scoring.scoring_engine import compute_master_score


def _make_trend(score: float = 160.0) -> TrendEngineResult:
    return TrendEngineResult(
        trend_score=score,
        trend_grade=TrendGrade.A,
        trend_state=TrendState.UP,
        trend_confidence=75.0,
        trend_risk=25.0,
        atomic_results={},
        composite_results={},
        reasons=["trend ok"],
    )


def test_engine_registry_complete():
    assert len(ENGINE_WEIGHTS) == 20
    assert MASTER_MAX_SCORE == 1000.0
    assert sum(weight for _, weight in ENGINE_WEIGHTS.values()) == 1270.0


def test_mvp_mode_includes_trend_and_pending_ma():
    trend = _make_trend(180.0)
    master = compute_master_score(trend, mvp_mode=True)

    assert master.total_score == 180.0
    assert master.max_score == 200.0
    assert master.mvp_mode is True
    assert master.domains["trend"] is not None
    assert master.domains["trend"].score == 180.0
    assert master.domains["moving_average"] is not None
    assert master.domains["moving_average"].status == "pending"
    assert master.domains["volume"] is not None
    assert master.domains["volume"].status == "pending"
    assert master.grade == "F"
    assert master.interpretation == "Reject"


def _make_ma(score: float = 120.0) -> MovingAverageEngineResult:
    return MovingAverageEngineResult(
        ma_score=score,
        ma_grade="A",
        ma_state="Bullish MA Structure",
        atomic_results={},
        reasons=["ma ok"],
    )


def test_mvp_mode_with_moving_average():
    trend = _make_trend(160.0)
    ma = _make_ma(130.0)
    master = compute_master_score(trend=trend, moving_average=ma, mvp_mode=True)
    assert master.total_score == 290.0
    assert master.max_score == 350.0
    assert master.domains["moving_average"].status == "implemented"
    assert master.domains["moving_average"].score == 130.0
    assert master.domains["volume"].status == "pending"


def _make_volume(score: float = 110.0) -> VolumeEngineResult:
    return VolumeEngineResult(
        vl_score=score,
        vl_grade="A",
        vl_state="Strong Volume Confirmation",
        atomic_results={},
        reasons=["volume ok"],
    )


def test_mvp_mode_with_all_three_domains():
    trend = _make_trend(160.0)
    ma = _make_ma(130.0)
    vol = _make_volume(120.0)
    master = compute_master_score(trend=trend, moving_average=ma, volume=vol, mvp_mode=True)
    assert master.total_score == 410.0
    assert master.max_score == 500.0
    assert master.domains["volume"].status == "implemented"


def test_full_mode_pending_domains_counted_in_breakdown():
    trend = _make_trend(150.0)
    master = compute_master_score(trend, mvp_mode=False)

    assert master.total_score == 150.0
    assert master.max_score == MASTER_MAX_SCORE
    assert master.domains["trend"] is not None
    assert master.domains["moving_average"] is not None
    assert master.domains["moving_average"].status == "pending"
    assert master.domains["data_quality"] is not None
    assert len(master.engine_breakdown) == len(ENGINE_WEIGHTS)


def test_engine_breakdown_fields():
    trend = _make_trend(100.0)
    master = compute_master_score(trend, mvp_mode=True)
    trend_row = next(row for row in master.engine_breakdown if row.engine_key == "trend")

    assert trend_row.engine_name == "Trend"
    assert trend_row.raw_score == 100.0
    assert trend_row.maximum_score == 200.0
    assert trend_row.normalized_score == pytest.approx(0.5)
    assert trend_row.weight == 200.0
    assert trend_row.contribution == 100.0
    assert trend_row.final_score == 100.0


def test_additional_domain_scores_are_aggregated():
    trend = _make_trend(100.0)
    extra = {
        "volume": DomainScore(score=75.0, max_score=150.0, status="implemented"),
        "momentum": DomainScore(score=60.0, max_score=150.0, status="implemented"),
    }
    master = compute_master_score(trend, domains=extra, mvp_mode=False)

    assert master.total_score == 235.0
    assert master.domains["volume"].score == 75.0
    assert master.domains["momentum"].score == 60.0


def test_domain_score_is_clamped_to_maximum():
    trend = _make_trend(250.0)
    master = compute_master_score(trend, mvp_mode=True)

    assert master.total_score == 200.0
    assert master.domains["trend"].score == 200.0


@pytest.mark.parametrize(
    ("score", "expected_grade", "expected_interpretation"),
    [
        (975.0, "SSS", "Exceptional Opportunity"),
        (920.0, "SS", "Excellent Opportunity"),
        (870.0, "S", "Strong Opportunity"),
        (820.0, "A", "Good Opportunity"),
        (770.0, "B", "Average Opportunity"),
        (720.0, "C", "Weak Opportunity"),
        (670.0, "D", "Reject"),
        (500.0, "F", "Reject"),
    ],
)
def test_master_grade_thresholds(score, expected_grade, expected_interpretation):
    grade = grade_from_score(score)
    assert grade.code == expected_grade
    assert interpretation_from_score(score) == expected_interpretation


def test_deterministic_output():
    trend = _make_trend(142.5)
    first = compute_master_score(trend, mvp_mode=True)
    second = compute_master_score(trend, mvp_mode=True)

    assert first.total_score == second.total_score
    assert first.grade == second.grade
    assert first.engine_breakdown == second.engine_breakdown
