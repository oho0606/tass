from __future__ import annotations

from pathlib import Path

import pandas as pd


class ParquetStore:
    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _path(self, symbol: str) -> Path:
        code = symbol.split(".")[0].zfill(6)
        return self.cache_dir / f"{code}.parquet"

    def save(self, symbol: str, df: pd.DataFrame) -> None:
        if df.empty:
            return
        df.to_parquet(self._path(symbol))

    def load(self, symbol: str) -> pd.DataFrame | None:
        path = self._path(symbol)
        if not path.exists():
            return None
        return pd.read_parquet(path)

    def merge_and_save(self, symbol: str, new_df: pd.DataFrame) -> pd.DataFrame:
        """Incremental update: merge new rows, dedupe by index, sort ascending."""
        if new_df.empty:
            existing = self.load(symbol)
            return existing if existing is not None else new_df

        existing = self.load(symbol)
        if existing is None or existing.empty:
            merged = new_df.copy()
        else:
            merged = pd.concat([existing, new_df])
            merged = merged[~merged.index.duplicated(keep="last")]
            merged = merged.sort_index()

        self.save(symbol, merged)
        return merged
