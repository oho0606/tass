from __future__ import annotations

import numpy as np
import pandas as pd


def make_uptrend_ohlcv(n: int = 80, start: float = 100.0) -> pd.DataFrame:
  """Synthetic uptrend with clear pivot highs/lows for rule evaluation."""
  dates = pd.date_range("2024-01-01", periods=n, freq="B")
  close = np.zeros(n)
  high = np.zeros(n)
  low = np.zeros(n)
  open_ = np.zeros(n)

  price = start
  for i in range(n):
    cycle = i % 10
    if cycle < 5:
      price += 1.2
    else:
      price -= 0.4
    close[i] = price
    high[i] = price + 2.0
    low[i] = price - 1.5
    open_[i] = price - 0.2

  volume = 1_000_000 + np.arange(n) * 8000
  return pd.DataFrame(
    {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
    index=dates,
  )


def make_downtrend_ohlcv(n: int = 80, start: float = 200.0) -> pd.DataFrame:
  dates = pd.date_range("2024-01-01", periods=n, freq="B")
  close = start - np.arange(n) * 0.9
  high = close + 1.0
  low = close - 1.5
  open_ = close + 0.2
  volume = 800_000 * np.ones(n)
  return pd.DataFrame(
    {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
    index=dates,
  )


def make_sideways_ohlcv(n: int = 80, mid: float = 100.0) -> pd.DataFrame:
  dates = pd.date_range("2024-01-01", periods=n, freq="B")
  close = mid + np.sin(np.arange(n) / 3) * 2
  high = close + 1.0
  low = close - 1.0
  open_ = close
  volume = 500_000 * np.ones(n)
  return pd.DataFrame(
    {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
    index=dates,
  )


def make_gap_up_ohlcv(n: int = 80, start: float = 100.0, gap: float = 8.0) -> pd.DataFrame:
  df = make_uptrend_ohlcv(n=n, start=start)
  if len(df) > 20:
    idx = df.index[20]
    prev_close = float(df.loc[df.index[19], "close"])
    open_price = prev_close + gap
    df.loc[idx, "open"] = open_price
    df.loc[idx, "high"] = open_price + 2.0
    df.loc[idx, "low"] = open_price - 1.0
    df.loc[idx, "close"] = open_price + 1.5
  return df


def make_high_volume_ohlcv(n: int = 80, start: float = 100.0) -> pd.DataFrame:
  df = make_uptrend_ohlcv(n=n, start=start)
  df["volume"] = 5_000_000 + np.arange(n) * 50_000
  if len(df) > 30:
    spike_idx = df.index[30]
    df.loc[spike_idx, "volume"] = 50_000_000
  return df
