from __future__ import annotations



from dataclasses import dataclass

from datetime import date, timedelta

from pathlib import Path



import pandas as pd



import engine.data.adapters.kis  # noqa: F401 — register adapters

import engine.data.adapters.yahoo  # noqa: F401

from engine.data.adapters.base import DataAdapter, get_adapter

from engine.data.pipeline import DataPipeline

from engine.data.store import ParquetStore

from engine.data.validator import DataValidationResult, validate_ohlcv





@dataclass

class DataEngineConfig:

    adapter_name: str = "yahoo"

    min_bars: int = 60

    cache_dir: Path = Path("data/cache")

    max_retries: int = 3

    retry_delay: int = 3

    enable_provider_fallback: bool = True





def _parse_krx_symbol(symbol: str) -> tuple[str, str] | None:

    """Return (code, market) for KRX equities, or None for indices/global symbols."""

    normalized = symbol.strip()

    if normalized.startswith("^"):

        return None

    if "." in normalized:

        code, suffix = normalized.rsplit(".", 1)

        market = "KQ" if suffix.upper() == "KQ" else "KS"

        return code.zfill(6), market

    if normalized.isdigit() and len(normalized) <= 6:

        return normalized.zfill(6), "KS"

    return None





class DataEngine:

    def __init__(self, config: DataEngineConfig | None = None):

        self.config = config or DataEngineConfig()

        self.adapter: DataAdapter = get_adapter(

            self.config.adapter_name,

            cache_dir=self.config.cache_dir,

            max_retries=self.config.max_retries,

            retry_delay=self.config.retry_delay,

            min_rows=self.config.min_bars,

        )

        self.store = ParquetStore(self.config.cache_dir)

        self.pipeline = DataPipeline(

            provider=self.config.adapter_name,

            enable_fallback=self.config.enable_provider_fallback,

            cache_dir=self.config.cache_dir,

            min_rows=self.config.min_bars,

        )



    def get_ohlcv(

        self,

        symbol: str,

        start: date | None = None,

        end: date | None = None,

        use_cache: bool = True,

    ) -> tuple[pd.DataFrame, DataValidationResult]:

        end = end or date.today()

        start = start or (end - timedelta(days=400))



        parsed = _parse_krx_symbol(symbol)

        if parsed is not None:

            code, market = parsed

            df = self.pipeline.get_validated_data(

                code,

                market,

                start.isoformat(),

                end.isoformat(),

            )

            if not df.empty:

                subset = df.loc[str(start) : str(end)]

                if len(subset) >= self.config.min_bars:

                    validation = validate_ohlcv(subset, min_bars=self.config.min_bars)

                    return subset, validation

                validation = validate_ohlcv(df, min_bars=self.config.min_bars)

                return df, validation



            if use_cache:

                cached = self.store.load(symbol)

                if cached is not None and len(cached) >= self.config.min_bars:

                    subset = cached.loc[str(start) : str(end)]

                    validation = validate_ohlcv(subset, min_bars=self.config.min_bars)

                    return subset, validation



            validation = validate_ohlcv(df, min_bars=self.config.min_bars)

            return df, validation



        if use_cache:

            cached = self.store.load(symbol)

            if cached is not None and len(cached) >= self.config.min_bars:

                subset = cached.loc[str(start) : str(end)]

                if len(subset) >= self.config.min_bars:

                    validation = validate_ohlcv(subset, min_bars=self.config.min_bars)

                    return subset, validation



        df = self.adapter.fetch_ohlcv(symbol, start, end)

        if not df.empty:

            self.store.save(symbol, df)

        validation = validate_ohlcv(df, min_bars=self.config.min_bars)

        return df, validation



    def update_cache(

        self,

        symbol: str,

        market: str,

        start_date: date,

        end_date: date | None = None,

    ) -> pd.DataFrame:

        """Prefetch or incrementally extend cached OHLCV for a symbol."""

        end_date = end_date or date.today()

        code = symbol.strip().split(".")[0].zfill(6)

        cached = self.store.load(code)



        if cached is not None and not cached.empty:

            last_cached = pd.to_datetime(cached.index.max()).date()

            if last_cached >= end_date:

                return cached

            fetch_start = last_cached + timedelta(days=1)

            if fetch_start > end_date:

                return cached

            return self.pipeline.get_validated_data(

                code,

                market,

                fetch_start.isoformat(),

                end_date.isoformat(),

            )



        return self.pipeline.get_validated_data(

            code,

            market,

            start_date.isoformat(),

            end_date.isoformat(),

        )


