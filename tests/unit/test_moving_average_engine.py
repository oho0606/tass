"""Unit tests for Moving Average Domain Engine."""

from __future__ import annotations

from engine.domains.moving_average_engine import evaluate_moving_average_engine
from engine.indicators.registry import compute_all
from engine.scoring import compute_master_score
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def test_moving_average_engine_score_range():
    df = compute_all(make_uptrend_ohlcv(n=260))
    result = evaluate_moving_average_engine(df)
    assert 0 <= result.ma_score <= 150
    assert result.ma_grade in {"S", "A", "B", "C", "D"}
    assert len(result.atomic_results) == 6


def test_master_score_includes_moving_average():
    from engine.domains.trend_engine import evaluate_trend_engine

    df = compute_all(make_uptrend_ohlcv(n=260))
    trend = evaluate_trend_engine(df)
    ma = evaluate_moving_average_engine(df)
    master = compute_master_score(trend=trend, moving_average=ma, mvp_mode=True)
    ma_domain = master.domains.get("moving_average")
    assert ma_domain is not None
    assert ma_domain.status == "implemented"
    assert master.max_score == 350.0
