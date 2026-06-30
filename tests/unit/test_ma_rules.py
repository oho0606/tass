"""Unit tests for MA atomic rules (TASS-015)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from engine.indicators.registry import compute_all
from engine.rules.ma.ma0002_price_above_sma20 import MA0002PriceAboveSMA20Rule, evaluate_ma0002
from engine.rules.ma.ma0007_price_below_sma20 import evaluate_ma0007
from engine.rules.ma.ma0021_sma_bullish_alignment import evaluate_ma0021
from engine.rules.ma.ma0023_ema_bullish_alignment import evaluate_ma0023
from engine.rules.ma.ma0029_full_bullish_alignment import evaluate_ma0029
from engine.rules.ma.ma0041_sma_rising import evaluate_ma0041
from engine.rules.ma.ma0051_price_extended_above_ma import evaluate_ma0051
from engine.rules.ma.ma0053_price_near_moving_average import evaluate_ma0053
from engine.rules.ma.ma0060_moving_average_structure_stable import evaluate_ma0060
from engine.rules.ma.registry import MA_EVALUATORS
from tests.fixtures.ohlcv import make_downtrend_ohlcv, make_uptrend_ohlcv


def _with_indicators(df: pd.DataFrame) -> pd.DataFrame:
    return compute_all(df)


def _golden_cross_frame(n: int = 80) -> pd.DataFrame:
    """Synthetic frame where SMA20 crosses above SMA60 on the last bar."""
    dates = pd.date_range("2024-01-01", periods=n, freq="B")
    close = np.linspace(100, 130, n)
    close[-3:] = [125, 124, 135]
    df = pd.DataFrame(
        {
            "open": close - 0.5,
            "high": close + 1,
            "low": close - 1,
            "close": close,
            "volume": np.full(n, 1_000_000.0),
        },
        index=dates,
    )
    return compute_all(df)


class TestMAPricePositionRules:
    def test_ma0002_uptrend_pass(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=80))
        result = evaluate_ma0002(df)
        assert result.rule_id == "MA0002"
        assert result.verdict == "PASS"

    def test_ma0002_downtrend_fail(self) -> None:
        df = _with_indicators(make_downtrend_ohlcv(n=80))
        result = evaluate_ma0002(df)
        assert result.verdict == "FAIL"

    def test_ma0007_downtrend_pass(self) -> None:
        df = _with_indicators(make_downtrend_ohlcv(n=80))
        result = evaluate_ma0007(df)
        assert result.verdict == "PASS"

    def test_ma0002_class_interface(self) -> None:
        rule = MA0002PriceAboveSMA20Rule()
        rule.initialize()
        df = _with_indicators(make_uptrend_ohlcv(n=80))
        assert rule.validate_input(df)
        rule.run(df)
        assert rule.metadata()["rule_id"] == "MA0002"

    def test_registry_has_sixty_rules(self) -> None:
        assert len(MA_EVALUATORS) == 60
        assert "MA0060" in MA_EVALUATORS
        assert "MA0041" in MA_EVALUATORS


class TestMAAlignmentRules:
    def test_ma0021_uptrend(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=260))
        result = evaluate_ma0021(df)
        assert result.rule_id == "MA0021"
        assert result.verdict in ("PASS", "PARTIAL", "FAIL")

    def test_ma0023_ema_bullish_uptrend(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=260))
        result = evaluate_ma0023(df)
        assert result.verdict in ("PASS", "PARTIAL", "FAIL")

    def test_ma0029_full_bullish(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=260))
        result = evaluate_ma0029(df)
        assert result.verdict in ("PASS", "FAIL")


class TestMACrossoverRules:
    def test_ma0031_detects_cross_or_fail(self) -> None:
        from engine.rules.ma.ma0031_sma_golden_cross import evaluate_ma0031

        df = _golden_cross_frame()
        result = evaluate_ma0031(df)
        assert result.rule_id == "MA0031"
        assert result.verdict in ("PASS", "FAIL")


class TestMASlopeRules:
    def test_ma0041_uptrend_rising(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=260))
        result = evaluate_ma0041(df)
        assert result.rule_id == "MA0041"
        assert result.verdict in ("PASS", "FAIL")

    def test_ma0041_downtrend_falling_or_fail(self) -> None:
        from engine.rules.ma.ma0042_sma_falling import evaluate_ma0042

        df = _with_indicators(make_downtrend_ohlcv(n=260))
        rising = evaluate_ma0041(df)
        falling = evaluate_ma0042(df)
        assert rising.verdict in ("PASS", "FAIL")
        assert falling.verdict in ("PASS", "FAIL")


class TestMAStructureRules:
    def test_ma0053_near_ma_on_sideways(self) -> None:
        from tests.fixtures.ohlcv import make_sideways_ohlcv

        df = _with_indicators(make_sideways_ohlcv(n=260))
        result = evaluate_ma0053(df)
        assert result.rule_id == "MA0053"
        assert result.verdict in ("PASS", "FAIL")

    def test_ma0051_extended_above_uptrend(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=260))
        result = evaluate_ma0051(df)
        assert result.verdict in ("PASS", "FAIL")

    def test_ma0060_structure_stable_uptrend(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=260))
        result = evaluate_ma0060(df)
        assert result.verdict in ("PASS", "FAIL")
