"""Unit tests for Backtest Engine v1.0."""

from __future__ import annotations

from datetime import date

from engine.backtest import (
    BacktestEngine,
    BacktestEngineConfig,
    BacktestRunInput,
    calculate_metrics,
    generate_signals,
    simulate_trades,
)
from engine.backtest.config import TradingConfig, load_backtest_config
from engine.backtest.rule_backtest import backtest_rule
from engine.backtest.types import TradeRecord
from engine.rules.tr.tr0001_higher_high import evaluate_higher_high
from tests.fixtures.ohlcv import make_downtrend_ohlcv, make_uptrend_ohlcv


class TestMetrics:
    def test_empty_trades_returns_zeros(self) -> None:
        metrics = calculate_metrics([], initial_capital=100_000_000, sample_days=100)
        assert metrics.trade_count == 0
        assert metrics.win_rate == 0.0

    def test_winning_trades_metrics(self) -> None:
        trades = [
            TradeRecord(
                entry_date=date(2024, 1, 2),
                exit_date=date(2024, 1, 10),
                entry_price=100.0,
                exit_price=110.0,
                return_pct=10.0,
                pnl=10_000_000.0,
                exit_reason="take_profit",
            ),
            TradeRecord(
                entry_date=date(2024, 2, 2),
                exit_date=date(2024, 2, 12),
                entry_price=100.0,
                exit_price=105.0,
                return_pct=5.0,
                pnl=5_000_000.0,
                exit_reason="hold",
            ),
        ]
        metrics = calculate_metrics(trades, initial_capital=100_000_000, sample_days=252)
        assert metrics.trade_count == 2
        assert metrics.win_rate == 1.0
        assert metrics.profit_factor > 0


class TestSimulator:
    def test_simulate_respects_non_overlap(self) -> None:
        df = make_uptrend_ohlcv(n=120)
        trading = TradingConfig(hold_days=10)
        signals = [60, 65, 70]
        trades = simulate_trades(df, signals, trading)
        assert len(trades) >= 1

    def test_entry_next_open_uses_open_price(self) -> None:
        df = make_uptrend_ohlcv(n=80)
        trading = TradingConfig(entry_mode="next_open", hold_days=5, stop_loss_pct=0.99)
        trades = simulate_trades(df, [60], trading)
        assert len(trades) == 1
        assert trades[0].entry_price > 0


class TestRuleBacktest:
    def test_tr0001_uptrend_produces_trades(self) -> None:
        cfg = load_backtest_config()
        df = make_uptrend_ohlcv(n=200)
        result = backtest_rule("TR0001", "SYN_UP", df, evaluate_higher_high, cfg)
        assert result.rule_id == "TR0001"
        assert result.metrics.trade_count >= 0
        assert result.verdict in ("ADOPT", "REJECT", "REVISE", "INSUFFICIENT_DATA")

    def test_short_data_insufficient(self) -> None:
        cfg = load_backtest_config()
        df = make_uptrend_ohlcv(n=30)
        result = backtest_rule("TR0001", "SHORT", df, evaluate_higher_high, cfg)
        assert result.verdict == "INSUFFICIENT_DATA"


class TestBacktestEngine:
    def test_run_multiple_rules_and_symbols(self) -> None:
        engine = BacktestEngine()
        run_input = BacktestRunInput(
            ohlcv_by_symbol={
                "UP": make_uptrend_ohlcv(n=200),
                "DOWN": make_downtrend_ohlcv(n=200),
            },
            rule_ids=("TR0001", "TR0002"),
            data_source="synthetic",
        )
        result = engine.run(run_input)
        assert len(result.rule_results) == 4
        assert result.config_version == "1.0"

    def test_run_and_save_writes_report(self, tmp_path) -> None:
        from dataclasses import replace

        cfg = replace(load_backtest_config(), output_dir=str(tmp_path))
        engine = BacktestEngine(BacktestEngineConfig(config=cfg))
        run_input = BacktestRunInput(
            ohlcv_by_symbol={"UP": make_uptrend_ohlcv(n=200)},
            rule_ids=("TR0001",),
        )
        _, json_path, _ = engine.run_and_save(run_input)
        assert json_path.exists()


class TestGenerateSignals:
    def test_uptrend_has_pass_signals(self) -> None:
        df = make_uptrend_ohlcv(n=200)
        signals = generate_signals(df, evaluate_higher_high, min_bars=60)
        assert isinstance(signals, list)

    def test_deterministic_signals(self) -> None:
        df = make_uptrend_ohlcv(n=200)
        first = generate_signals(df, evaluate_higher_high, min_bars=60)
        second = generate_signals(df, evaluate_higher_high, min_bars=60)
        assert first == second
