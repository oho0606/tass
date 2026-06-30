"""Shared helpers for VL volume atomic rules."""

from __future__ import annotations

import pandas as pd

DEFAULT_N_PERIOD = 20
EQUAL_TOLERANCE_PCT = 2.0
AT_EXTREME_TOLERANCE_PCT = 0.5
SPIKE_MULTIPLIER = 2.0
SPIKE_THRESHOLD = 2.5
SUDDEN_CHANGE_PCT = 50.0
SLOPE_LOOKBACK = 5
FLAT_SLOPE_THRESHOLD_PCT = 2.0
CONSECUTIVE_BARS = 3
RELATIVE_THRESHOLD = 1.5
MONEY_FLOW_LOOKBACK = 5


def validate_volume_df(df: pd.DataFrame, *, min_bars: int = DEFAULT_N_PERIOD) -> bool:
    """Return True when volume OHLCV columns are usable."""
    if df is None or df.empty or len(df) < min_bars:
        return False
    required = ("volume", "close", "open")
    if any(col not in df.columns for col in required):
        return False
    return not pd.isna(df["volume"].iloc[-min_bars:]).any()


def volume_avg(df: pd.DataFrame, period: int = DEFAULT_N_PERIOD) -> float:
    """N-period average volume."""
    if "volume_ma_20" in df.columns and period == DEFAULT_N_PERIOD:
        return float(df["volume_ma_20"].iloc[-1])
    return float(df["volume"].rolling(period).mean().iloc[-1])


def relative_volume_value(df: pd.DataFrame, period: int = DEFAULT_N_PERIOD) -> float:
    """Relative volume vs N-period average."""
    if "relative_volume" in df.columns:
        return float(df["relative_volume"].iloc[-1])
    avg = volume_avg(df, period)
    if avg == 0.0:
        return 0.0
    return float(df["volume"].iloc[-1]) / avg


def period_high(df: pd.DataFrame, period: int = DEFAULT_N_PERIOD) -> float:
    """N-period volume high."""
    if "volume_high_20" in df.columns and period == DEFAULT_N_PERIOD:
        return float(df["volume_high_20"].iloc[-1])
    return float(df["volume"].rolling(period).max().iloc[-1])


def period_low(df: pd.DataFrame, period: int = DEFAULT_N_PERIOD) -> float:
    """N-period volume low."""
    if "volume_low_20" in df.columns and period == DEFAULT_N_PERIOD:
        return float(df["volume_low_20"].iloc[-1])
    return float(df["volume"].rolling(period).min().iloc[-1])


def is_up_bar(df: pd.DataFrame, index: int = -1) -> bool:
    """Return True when close >= open for the indexed bar."""
    return float(df["close"].iloc[index]) >= float(df["open"].iloc[index])


def is_down_bar(df: pd.DataFrame, index: int = -1) -> bool:
    """Return True when close < open for the indexed bar."""
    return float(df["close"].iloc[index]) < float(df["open"].iloc[index])


def volume_slope_pct(series: pd.Series, lookback: int = SLOPE_LOOKBACK) -> float:
    """Percent volume change over lookback bars."""
    if len(series) <= lookback:
        return 0.0
    start = float(series.iloc[-lookback - 1])
    end = float(series.iloc[-1])
    if start == 0.0:
        return 0.0
    return (end - start) / start * 100.0


def near_equal(left: float, right: float, tolerance_pct: float = EQUAL_TOLERANCE_PCT) -> bool:
    """Return True when values are within tolerance percent."""
    if right == 0.0:
        return left == 0.0
    return abs((left - right) / right * 100.0) <= tolerance_pct
