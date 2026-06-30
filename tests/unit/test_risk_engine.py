"""Unit tests for Risk Engine v1.0."""

from __future__ import annotations

from engine.core.types import GateResult, MasterScoreResult
from engine.domains.trend_engine import evaluate_trend_engine
from engine.gate.basic_gate import GateConfig, evaluate_basic_gate
from engine.indicators.registry import compute_all
from engine.risk import compute_risk, decision_from_score, grade_from_score, level_from_score
from engine.risk.mapping import DEFAULT_COMPONENT_WEIGHTS
from tests.fixtures.ohlcv import make_downtrend_ohlcv, make_uptrend_ohlcv


def _master(score: float = 150.0) -> MasterScoreResult:
    return MasterScoreResult(
        total_score=score,
        max_score=1000.0,
        mvp_mode=True,
        domains={},
    )


def _evaluate(df):
    df = compute_all(df)
    trend = evaluate_trend_engine(df)
    gate = evaluate_basic_gate(
        df, trend, data_valid=True, config=GateConfig(min_traded_value_ma20=0, trend_floor_score=0)
    )
    risk = compute_risk(df, trend, _master(), gate=gate, data_valid=True)
    return df, trend, gate, risk


def test_component_weights_sum_to_100():
    total = sum(c.weight for c in DEFAULT_COMPONENT_WEIGHTS)
    assert total == 100


def test_same_inputs_same_risk():
    df = make_uptrend_ohlcv()
    df = compute_all(df)
    trend = evaluate_trend_engine(df)
    master = _master()
    first = compute_risk(df, trend, master, data_valid=True)
    second = compute_risk(df, trend, master, data_valid=True)
    assert first == second


def test_risk_score_bounded():
    _, _, _, risk = _evaluate(make_uptrend_ohlcv())
    assert 0.0 <= risk.risk_score <= 100.0


def test_uptrend_lower_risk_than_downtrend():
    _, _, _, up = _evaluate(make_uptrend_ohlcv())
    _, _, _, down = _evaluate(make_downtrend_ohlcv())
    assert up.risk_score < down.risk_score


def test_explainability_fields():
    _, _, _, risk = _evaluate(make_uptrend_ohlcv())
    assert risk.config_version == "1.0"
    assert len(risk.components) == 14
    assert len(risk.reasons) >= 3
    assert risk.risk_grade
    assert risk.risk_level
    assert risk.risk_decision in {"PASS", "PASS WITH CAUTION", "REVIEW REQUIRED", "FAIL"}


def test_grade_boundaries():
    assert grade_from_score(5.0).label == "Very Low Risk"
    assert grade_from_score(15.0).label == "Low Risk"
    assert grade_from_score(20.0).label == "Low Risk"
    assert grade_from_score(20.11).label == "Moderate Risk"
    assert grade_from_score(25.0).label == "Moderate Risk"
    assert grade_from_score(35.0).label == "Elevated Risk"
    assert grade_from_score(45.0).label == "High Risk"
    assert grade_from_score(60.0).label == "Very High Risk"
    assert grade_from_score(80.0).label == "Extreme Risk"


def test_level_boundaries():
    assert level_from_score(8.0).label == "Excellent"
    assert level_from_score(18.0).label == "Good"
    assert level_from_score(28.0).label == "Acceptable"
    assert level_from_score(38.0).label == "Caution"
    assert level_from_score(48.0).label == "Danger"
    assert level_from_score(55.0).label == "Reject"


def test_decision_boundaries():
    assert decision_from_score(10.0) == "PASS"
    assert decision_from_score(25.0) == "PASS WITH CAUTION"
    assert decision_from_score(35.0) == "REVIEW REQUIRED"
    assert decision_from_score(45.0) == "FAIL"


def test_data_quality_increases_risk():
    df = make_uptrend_ohlcv()
    df = compute_all(df)
    trend = evaluate_trend_engine(df)
    master = _master()
    clean = compute_risk(df, trend, master, data_valid=True)
    dirty = compute_risk(
        df,
        trend,
        master,
        data_valid=False,
        gate=GateResult(status="FAIL", failed_gates=["DataQuality"]),
    )
    assert dirty.risk_score > clean.risk_score


def test_does_not_modify_master_score():
    master = _master(175.0)
    df = compute_all(make_uptrend_ohlcv())
    trend = evaluate_trend_engine(df)
    compute_risk(df, trend, master)
    assert master.total_score == 175.0


def test_component_breakdown_contributions():
    _, _, _, risk = _evaluate(make_uptrend_ohlcv())
    total = round(sum(c.contribution for c in risk.components), 2)
    assert total == risk.risk_score
