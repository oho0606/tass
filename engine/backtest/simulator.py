"""Trade simulation with fees and slippage (TASS-009 §7)."""

from __future__ import annotations

from datetime import date

import pandas as pd

from engine.backtest.config import TradingConfig
from engine.backtest.types import TradeRecord


def simulate_trades(
    df: pd.DataFrame,
    signal_indices: list[int],
    trading: TradingConfig,
) -> list[TradeRecord]:
    """Simulate non-overlapping trades from rule PASS signals.

    Args:
        df: OHLCV DataFrame with DatetimeIndex.
        signal_indices: Bar indices where rule verdict is PASS.
        trading: Commission, slippage, hold, stop/take-profit settings.

    Returns:
        List of closed ``TradeRecord`` instances.

    Example:
        >>> trades = simulate_trades(df, [60, 90], TradingConfig())
    """
    if df.empty or not signal_indices:
        return []

    trades: list[TradeRecord] = []
    position_exit_idx = -1
    sorted_signals = sorted(signal_indices)

    for signal_idx in sorted_signals:
        if signal_idx <= position_exit_idx:
            continue
        entry_idx = _resolve_entry_index(df, signal_idx, trading.entry_mode)
        if entry_idx >= len(df):
            continue

        trade = _simulate_single_trade(df, entry_idx, trading)
        if trade is None:
            continue
        trades.append(trade)
        position_exit_idx = _index_of_date(df, trade.exit_date)

    return trades


def _resolve_entry_index(df: pd.DataFrame, signal_idx: int, entry_mode: str) -> int:
    """Map signal bar to entry bar index."""
    if entry_mode == "next_open":
        return signal_idx + 1
    return signal_idx


def _simulate_single_trade(
    df: pd.DataFrame,
    entry_idx: int,
    trading: TradingConfig,
) -> TradeRecord | None:
    """Simulate one trade from entry bar until exit."""
    if entry_idx >= len(df):
        return None

    entry_row = df.iloc[entry_idx]
    entry_price = float(
        entry_row["open"] if trading.entry_mode == "next_open" else entry_row["close"]
    )
    entry_price = _apply_entry_cost(entry_price, trading)

    stop_price = entry_price * (1.0 - trading.stop_loss_pct)
    target_price = entry_price * (1.0 + trading.take_profit_pct)
    max_exit_idx = min(entry_idx + trading.hold_days, len(df) - 1)

    exit_idx = max_exit_idx
    exit_reason = "hold"
    for idx in range(entry_idx + 1, max_exit_idx + 1):
        row = df.iloc[idx]
        low = float(row["low"])
        high = float(row["high"])
        if low <= stop_price:
            exit_idx = idx
            exit_reason = "stop_loss"
            exit_price = stop_price
            break
        if high >= target_price:
            exit_idx = idx
            exit_reason = "take_profit"
            exit_price = target_price
            break
    else:
        exit_price = float(df.iloc[exit_idx]["close"])

    exit_price = _apply_exit_cost(exit_price, trading)
    return_pct = ((exit_price / entry_price) - 1.0) * 100.0
    position_size = trading.initial_capital
    pnl = position_size * (exit_price / entry_price - 1.0)

    return TradeRecord(
        entry_date=_to_date(df.index[entry_idx]),
        exit_date=_to_date(df.index[exit_idx]),
        entry_price=round(entry_price, 4),
        exit_price=round(exit_price, 4),
        return_pct=round(return_pct, 4),
        pnl=round(pnl, 2),
        exit_reason=exit_reason,
    )


def _apply_entry_cost(price: float, trading: TradingConfig) -> float:
    """Apply slippage and commission on entry."""
    slipped = price * (1.0 + trading.slippage_rate)
    return slipped * (1.0 + trading.commission_rate)


def _apply_exit_cost(price: float, trading: TradingConfig) -> float:
    """Apply slippage and commission on exit."""
    slipped = price * (1.0 - trading.slippage_rate)
    return slipped * (1.0 - trading.commission_rate)


def _to_date(index_value: object) -> date:
    """Convert DataFrame index value to ``date``."""
    return pd.Timestamp(index_value).date()


def _index_of_date(df: pd.DataFrame, target: date) -> int:
    """Find last bar index matching exit date."""
    for idx in range(len(df) - 1, -1, -1):
        if _to_date(df.index[idx]) == target:
            return idx
    return len(df) - 1
