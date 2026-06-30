"""Unit tests for TASS-030 core infrastructure."""

from __future__ import annotations

from pathlib import Path

from config.app_settings import AppSettings, get_settings
from engine.core.exceptions import (
    BacktestException,
    DataException,
    EngineException,
    RecommendationException,
    RuleException,
    TassError,
)


class TestExceptions:
    def test_tass_error_carries_context(self) -> None:
        err = RuleException("rule failed", context={"rule_id": "TR0001"})
        assert err.message == "rule failed"
        assert err.context["rule_id"] == "TR0001"

    def test_exception_hierarchy(self) -> None:
        assert issubclass(RuleException, TassError)
        assert issubclass(EngineException, TassError)
        assert issubclass(DataException, TassError)
        assert issubclass(BacktestException, TassError)
        assert issubclass(RecommendationException, TassError)


class TestAppSettings:
    def test_defaults(self) -> None:
        settings = AppSettings()
        assert settings.log_level == "INFO"
        assert settings.timezone == "Asia/Seoul"
        assert settings.log_dir == Path("logs")

    def test_get_settings_cached(self) -> None:
        get_settings.cache_clear()
        first = get_settings()
        second = get_settings()
        assert first is second


class TestBacktestEngine:
    def test_run_produces_results(self) -> None:
        from engine.backtest import BacktestEngine, BacktestRunInput
        from tests.fixtures.ohlcv import make_uptrend_ohlcv

        engine = BacktestEngine()
        result = engine.run(
            BacktestRunInput(
                ohlcv_by_symbol={"UP": make_uptrend_ohlcv(n=200)},
                rule_ids=("TR0001",),
            )
        )
        assert len(result.rule_results) == 1
        assert result.rule_results[0].rule_id == "TR0001"
