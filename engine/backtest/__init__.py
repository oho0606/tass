"""Backtest Engine v1.0 (TASS-009)."""

from engine.backtest.backtest_engine import BacktestEngine, BacktestEngineConfig, BacktestRunInput
from engine.backtest.config import BacktestEngineConfigData, load_backtest_config
from engine.backtest.metrics import calculate_metrics
from engine.backtest.registry import RULE_EVALUATORS, get_rule_evaluator
from engine.backtest.rule_backtest import backtest_rule, generate_signals
from engine.backtest.simulator import simulate_trades
from engine.backtest.types import (
    BacktestMetrics,
    BacktestRunResult,
    BacktestVerdict,
    RuleBacktestResult,
    TradeRecord,
)

__all__ = [
    "BacktestEngine",
    "BacktestEngineConfig",
    "BacktestEngineConfigData",
    "BacktestMetrics",
    "BacktestRunInput",
    "BacktestRunResult",
    "BacktestVerdict",
    "RULE_EVALUATORS",
    "RuleBacktestResult",
    "TradeRecord",
    "backtest_rule",
    "calculate_metrics",
    "generate_signals",
    "get_rule_evaluator",
    "load_backtest_config",
    "simulate_trades",
]
