"""Rule-level walk-forward backtest runner (TASS-009 §9)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.backtest.config import BacktestEngineConfigData
from engine.backtest.metrics import calculate_metrics
from engine.backtest.simulator import simulate_trades
from engine.backtest.types import (
    BacktestMetrics,
    BacktestVerdict,
    RuleBacktestResult,
    SplitMetrics,
    TradeRecord,
)
from engine.core.types import RuleResult

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]


def generate_signals(
    df: pd.DataFrame,
    evaluator: RuleEvaluator,
    min_bars: int,
) -> list[int]:
    """Walk-forward PASS signal indices for a rule evaluator.

    Args:
        df: Full OHLCV history.
        evaluator: Callable returning ``RuleResult``.
        min_bars: Minimum history before first evaluation.

    Returns:
        Bar indices where verdict is PASS.
    """
    signals: list[int] = []
    for idx in range(min_bars, len(df)):
        window = df.iloc[: idx + 1].copy()
        result = evaluator(window)
        if result.verdict == "PASS":
            signals.append(idx)
    return signals


def backtest_rule(
    rule_id: str,
    symbol: str,
    df: pd.DataFrame,
    evaluator: RuleEvaluator,
    config: BacktestEngineConfigData,
) -> RuleBacktestResult:
    """Run backtest for one rule on one symbol's OHLCV.

    Args:
        rule_id: Canonical rule identifier (e.g. TR0001).
        symbol: Ticker symbol label for reporting.
        df: OHLCV DataFrame.
        evaluator: Rule evaluation callable.
        config: Backtest engine configuration.

    Returns:
        ``RuleBacktestResult`` with metrics, trades, and adoption verdict.
    """
    min_bars = config.evaluation.min_bars
    if len(df) < min_bars + 5:
        return _insufficient_data_result(rule_id, symbol, config.version, len(df))

    split_idx = int(len(df) * config.evaluation.in_sample_ratio)
    in_sample_df = df.iloc[:split_idx].copy()
    out_sample_df = df.iloc[split_idx:].copy()

    in_trades = _run_segment(in_sample_df, evaluator, config)
    out_trades = _run_segment(out_sample_df, evaluator, config)
    all_trades = _run_segment(df, evaluator, config)

    in_metrics = calculate_metrics(
        in_trades,
        initial_capital=config.trading.initial_capital,
        sample_days=len(in_sample_df),
    )
    out_metrics = calculate_metrics(
        out_trades,
        initial_capital=config.trading.initial_capital,
        sample_days=len(out_sample_df),
    )
    metrics = calculate_metrics(
        all_trades,
        initial_capital=config.trading.initial_capital,
        sample_days=len(df),
    )
    split_metrics = SplitMetrics(in_sample=in_metrics, out_of_sample=out_metrics)
    verdict, reasons = _evaluate_verdict(metrics, split_metrics, config)

    return RuleBacktestResult(
        rule_id=rule_id,
        symbol=symbol,
        metrics=metrics,
        split_metrics=split_metrics,
        trades=all_trades,
        verdict=verdict,
        reasons=reasons,
        version=config.version,
    )


def _run_segment(
    df: pd.DataFrame,
    evaluator: RuleEvaluator,
    config: BacktestEngineConfigData,
) -> list[TradeRecord]:
    """Generate signals and simulate trades for one data segment."""
    if len(df) < config.evaluation.min_bars + 2:
        return []
    signals = generate_signals(df, evaluator, config.evaluation.min_bars)
    return simulate_trades(df, signals, config.trading)


def _evaluate_verdict(
    metrics: BacktestMetrics,
    split_metrics: SplitMetrics,
    config: BacktestEngineConfigData,
) -> tuple[BacktestVerdict, list[str]]:
    """Determine ADOPT / REJECT / REVISE from TASS-009 criteria."""
    reasons: list[str] = []
    evaluation = config.evaluation

    if metrics.trade_count < evaluation.min_trades:
        reasons.append(f"거래 횟수 부족 ({metrics.trade_count} < {evaluation.min_trades})")
        return "INSUFFICIENT_DATA", reasons

    if metrics.win_rate < evaluation.min_win_rate:
        reasons.append(f"승률 미달 ({metrics.win_rate:.2%} < {evaluation.min_win_rate:.2%})")

    if metrics.max_drawdown_pct > evaluation.max_drawdown_pct * 100:
        reasons.append(
            f"MDD 초과 ({metrics.max_drawdown_pct:.2f}% > {evaluation.max_drawdown_pct * 100:.2f}%)"
        )

    out = split_metrics.out_of_sample
    if out.trade_count >= 1 and out.win_rate < metrics.win_rate * 0.8:
        reasons.append("Out-of-sample 승률 급락 — 과최적화 의심")

    if not reasons:
        reasons.append("TASS-009 기준 충족")
        return "ADOPT", reasons

    if metrics.profit_factor >= 1.0 and metrics.win_rate >= evaluation.min_win_rate * 0.9:
        reasons.append("부분 개선 — Rule 재검토 권고")
        return "REVISE", reasons

    return "REJECT", reasons


def _insufficient_data_result(
    rule_id: str,
    symbol: str,
    version: str,
    bar_count: int,
) -> RuleBacktestResult:
    """Return placeholder result when history is too short."""
    empty = calculate_metrics([], initial_capital=0.0, sample_days=bar_count)
    return RuleBacktestResult(
        rule_id=rule_id,
        symbol=symbol,
        metrics=empty,
        split_metrics=None,
        trades=[],
        verdict="INSUFFICIENT_DATA",
        reasons=[f"데이터 부족 ({bar_count} bars)"],
        version=version,
    )
