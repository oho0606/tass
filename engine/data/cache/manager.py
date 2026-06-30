from __future__ import annotations

from pathlib import Path

import pandas as pd

from engine.data.store import ParquetStore


class CacheManager:
    """Parquet-backed OHLCV cache with incremental merge support."""

    def __init__(self, cache_dir: Path | str = "data/cache") -> None:
        self.store = ParquetStore(Path(cache_dir))

    def load(self, symbol: str) -> pd.DataFrame | None:
        return self.store.load(symbol)

    def is_up_to_date(self, cached_df: pd.DataFrame | None, end_date: str) -> bool:
        if cached_df is None or cached_df.empty:
            return False
        last_cached = pd.to_datetime(cached_df.index.max()).date()
        target = pd.to_datetime(end_date).date()
        return last_cached >= target

    def merge_and_save(
        self,
        symbol: str,
        cached_df: pd.DataFrame | None,
        raw_df: pd.DataFrame,
    ) -> pd.DataFrame:
        if raw_df is None or raw_df.empty:
            return cached_df if cached_df is not None else pd.DataFrame()

        if cached_df is None or cached_df.empty:
            self.store.save(symbol, raw_df)
            return raw_df

        merged = pd.concat([cached_df, raw_df])
        merged = merged[~merged.index.duplicated(keep="last")].sort_index()
        self.store.save(symbol, merged)
        return merged
