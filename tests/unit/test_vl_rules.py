"""Unit tests for VL atomic rules (TASS-017)."""

from __future__ import annotations

from engine.indicators.registry import compute_all
from engine.rules.vl.registry import VL_EVALUATORS
from engine.rules.vl.vl0001_volume_above_n_period_average import evaluate_vl0001
from engine.rules.vl.vl0021_volume_rising import evaluate_vl0021
from engine.rules.vl.vl0041_up_bar_volume_above_average import evaluate_vl0041
from engine.rules.vl.vl0047_price_up_volume_up import evaluate_vl0047
from engine.rules.vl.vl0051_obv_rising import evaluate_vl0051
from tests.fixtures.ohlcv import make_downtrend_ohlcv, make_uptrend_ohlcv


def _with_indicators(df):
    return compute_all(df)


class TestVLAbsoluteRules:
    def test_vl0001_uptrend(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=80))
        result = evaluate_vl0001(df)
        assert result.rule_id == "VL0001"
        assert result.verdict in ("PASS", "FAIL")

    def test_registry_has_sixty_rules(self) -> None:
        assert len(VL_EVALUATORS) == 60
        assert "VL0060" in VL_EVALUATORS


class TestVLTrendRules:
    def test_vl0021_uptrend(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=80))
        result = evaluate_vl0021(df)
        assert result.verdict in ("PASS", "FAIL")


class TestVLConfirmationRules:
    def test_vl0041_and_vl0047(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=80))
        r1 = evaluate_vl0041(df)
        r2 = evaluate_vl0047(df)
        assert r1.verdict in ("PASS", "FAIL")
        assert r2.verdict in ("PASS", "FAIL")


class TestVLQualityRules:
    def test_vl0051_obv(self) -> None:
        df = _with_indicators(make_uptrend_ohlcv(n=80))
        result = evaluate_vl0051(df)
        assert result.verdict in ("PASS", "FAIL")

    def test_vl0051_downtrend(self) -> None:
        df = _with_indicators(make_downtrend_ohlcv(n=80))
        result = evaluate_vl0051(df)
        assert result.verdict in ("PASS", "FAIL")
