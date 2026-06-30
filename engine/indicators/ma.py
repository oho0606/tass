"""Moving average indicator calculations."""

from __future__ import annotations

import pandas as pd


def compute_ma(series: pd.Series, period: int) -> pd.Series:
    """Simple moving average with full-period minimum."""
    return series.rolling(window=period, min_periods=period).mean()


def compute_ema(series: pd.Series, period: int) -> pd.Series:
    """Exponential moving average."""
    return series.ewm(span=period, adjust=False, min_periods=period).mean()
