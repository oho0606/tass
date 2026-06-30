"""Performance metrics calculator (TASS-009 §8)."""

from __future__ import annotations

import math

import numpy as np

from engine.backtest.types import BacktestMetrics, TradeRecord

_TRADING_DAYS_PER_YEAR = 252


def calculate_metrics(
    trades: list[TradeRecord],
    *,
    initial_capital: float,
    sample_days: int,
) -> BacktestMetrics:
    """Compute backtest performance metrics from trade records.

    Args:
        trades: Closed trade list.
        initial_capital: Starting capital in KRW.
        sample_days: Calendar/trading days in the evaluation window.

    Returns:
        ``BacktestMetrics`` with all TASS-009 required fields.

    Example:
        >>> metrics = calculate_metrics([], initial_capital=1e8, sample_days=100)
        >>> metrics.trade_count
        0
    """
    if not trades:
        return BacktestMetrics(
            total_return_pct=0.0,
            cagr_pct=0.0,
            win_rate=0.0,
            avg_win_pct=0.0,
            avg_loss_pct=0.0,
            reward_risk_ratio=0.0,
            profit_factor=0.0,
            max_drawdown_pct=0.0,
            sharpe_ratio=0.0,
            sortino_ratio=0.0,
            trade_count=0,
            sample_days=sample_days,
        )

    returns = np.array([trade.return_pct for trade in trades], dtype=float)
    wins = returns[returns > 0]
    losses = returns[returns < 0]

    win_rate = float(len(wins) / len(returns))
    avg_win = float(np.mean(wins)) if len(wins) else 0.0
    avg_loss = float(np.mean(losses)) if len(losses) else 0.0
    reward_risk = abs(avg_win / avg_loss) if avg_loss != 0 else 0.0

    gross_profit = float(np.sum(wins)) if len(wins) else 0.0
    gross_loss = abs(float(np.sum(losses))) if len(losses) else 0.0
    if gross_loss > 0:
        profit_factor = gross_profit / gross_loss
    elif gross_profit > 0:
        profit_factor = 999.0
    else:
        profit_factor = 0.0

    equity = _build_equity_curve(trades, initial_capital)
    total_return_pct = ((equity[-1] / initial_capital) - 1.0) * 100.0
    cagr_pct = _calculate_cagr(initial_capital, equity[-1], sample_days)
    max_drawdown_pct = _calculate_max_drawdown(equity) * 100.0
    sharpe_ratio = _calculate_sharpe(returns)
    sortino_ratio = _calculate_sortino(returns)

    return BacktestMetrics(
        total_return_pct=round(total_return_pct, 4),
        cagr_pct=round(cagr_pct, 4),
        win_rate=round(win_rate, 4),
        avg_win_pct=round(avg_win, 4),
        avg_loss_pct=round(avg_loss, 4),
        reward_risk_ratio=round(reward_risk, 4),
        profit_factor=round(profit_factor, 4),
        max_drawdown_pct=round(max_drawdown_pct, 4),
        sharpe_ratio=round(sharpe_ratio, 4),
        sortino_ratio=round(sortino_ratio, 4),
        trade_count=len(trades),
        sample_days=sample_days,
    )


def _build_equity_curve(trades: list[TradeRecord], initial_capital: float) -> np.ndarray:
    """Build cumulative equity curve from sequential trades."""
    equity = [initial_capital]
    for trade in trades:
        equity.append(equity[-1] + trade.pnl)
    return np.array(equity, dtype=float)


def _calculate_cagr(initial: float, final: float, sample_days: int) -> float:
    """Annualized growth rate from sample period."""
    if sample_days <= 0 or initial <= 0 or final <= 0:
        return 0.0
    years = sample_days / _TRADING_DAYS_PER_YEAR
    if years <= 0:
        return 0.0
    return (math.pow(final / initial, 1.0 / years) - 1.0) * 100.0


def _calculate_max_drawdown(equity: np.ndarray) -> float:
    """Maximum peak-to-trough drawdown as a fraction."""
    if len(equity) < 2:
        return 0.0
    peak = equity[0]
    max_dd = 0.0
    for value in equity:
        if value > peak:
            peak = value
        if peak > 0:
            drawdown = (peak - value) / peak
            max_dd = max(max_dd, drawdown)
    return max_dd


def _calculate_sharpe(returns: np.ndarray) -> float:
    """Annualized Sharpe ratio from per-trade returns."""
    if len(returns) < 2:
        return 0.0
    std = float(np.std(returns, ddof=1))
    if std == 0:
        return 0.0
    return float(np.mean(returns) / std * math.sqrt(_TRADING_DAYS_PER_YEAR))


def _calculate_sortino(returns: np.ndarray) -> float:
    """Annualized Sortino ratio using downside deviation."""
    if len(returns) < 2:
        return 0.0
    downside = returns[returns < 0]
    if len(downside) == 0:
        return 0.0
    downside_std = float(np.std(downside, ddof=1))
    if downside_std == 0:
        return 0.0
    return float(np.mean(returns) / downside_std * math.sqrt(_TRADING_DAYS_PER_YEAR))
