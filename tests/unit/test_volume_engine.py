"""Unit tests for Volume Domain Engine."""

from __future__ import annotations

from engine.domains.trend_engine import evaluate_trend_engine
from engine.domains.volume_engine import evaluate_volume_engine
from engine.indicators.registry import compute_all
from engine.scoring import compute_master_score
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def test_volume_engine_score_range():
    df = compute_all(make_uptrend_ohlcv(n=260))
    result = evaluate_volume_engine(df)
    assert 0 <= result.vl_score <= 150
    assert result.vl_grade in {"S", "A", "B", "C", "D"}
    assert len(result.atomic_results) == 6


def test_master_score_includes_volume():
    df = compute_all(make_uptrend_ohlcv(n=260))
    trend = evaluate_trend_engine(df)
    volume = evaluate_volume_engine(df)
    master = compute_master_score(trend=trend, volume=volume, mvp_mode=True)
    vol_domain = master.domains.get("volume")
    assert vol_domain is not None
    assert vol_domain.status == "implemented"
    assert master.max_score == 350.0
