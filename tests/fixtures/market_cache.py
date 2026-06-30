"""Helpers to seed parquet OHLCV cache for offline KRX backtest tests."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from engine.data.adapters.yahoo import YahooAdapter
from engine.data.store import ParquetStore
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def seed_krx_cache(cache_dir: Path, *, bars: int = 400) -> dict[str, pd.DataFrame]:
    """Write synthetic long-history OHLCV into cache for mini KRX universe."""
    store = ParquetStore(cache_dir)
    adapter = YahooAdapter()
    frames: dict[str, pd.DataFrame] = {}

    for symbol, market in (("005930", "KS"), ("086520", "KQ")):
        df = make_uptrend_ohlcv(n=bars, start=50_000 + len(symbol))
        dates = pd.date_range(end=pd.Timestamp.today(), periods=bars, freq="B")
        df.index = dates
        yahoo_sym = adapter.to_yahoo_symbol(symbol, market)
        store.save(yahoo_sym, df)
        frames[symbol] = df

    return frames
