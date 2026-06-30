from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from engine.data.cache.manager import CacheManager
from engine.data.interfaces import IDataProvider
from engine.data.providers.kis_provider import KISProvider
from engine.data.providers.pykrx_provider import PyKRXProvider
from engine.data.providers.yahoo_provider import YahooFinanceProvider
from engine.data.resilience import ProviderFallbackChain
from engine.data.validators import DataQualityValidator

_MARKET_SUFFIX = {
    "KOSPI": "KS",
    "KOSDAQ": "KQ",
    "KS": "KS",
    "KQ": "KQ",
}


def _build_ohlcv_provider(
    provider_name: str,
    *,
    enable_fallback: bool,
) -> IDataProvider | ProviderFallbackChain:
    normalized = provider_name.strip().lower()
    yahoo = YahooFinanceProvider()

    if normalized == "kis":
        try:
            kis = KISProvider()
        except ValueError as exc:
            if enable_fallback:
                logging.getLogger("DataPipeline").warning(
                    "KIS not configured (%s); using Yahoo provider.", exc
                )
                return yahoo
            raise
        if enable_fallback:
            return ProviderFallbackChain(kis, yahoo)
        return kis

    return yahoo


class DataPipeline:
    """Cache -> fetch -> validate -> persist data flow orchestrator."""

    def __init__(
        self,
        provider: str = "yahoo",
        *,
        use_kis: bool | None = None,
        enable_fallback: bool = True,
        cache_dir: Path | str = "data/cache",
        min_rows: int = 120,
    ) -> None:
        self.logger = logging.getLogger("DataPipeline")
        self.meta_provider = PyKRXProvider()

        if use_kis is not None:
            provider = "kis" if use_kis else "yahoo"

        self.ohlcv_provider = _build_ohlcv_provider(provider, enable_fallback=enable_fallback)
        self.validator = DataQualityValidator(min_rows=min_rows)
        self.cache = CacheManager(cache_dir)

    def get_validated_data(
        self,
        symbol: str,
        market: str,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:
        code = symbol.strip().split(".")[0].zfill(6)
        cached_df = self.cache.load(code)
        if self.cache.is_up_to_date(cached_df, end_date):
            return cached_df

        provider_symbol = self._provider_symbol(code, market)
        try:
            raw_df = self.ohlcv_provider.fetch_ohlcv(provider_symbol, start_date, end_date)
        except Exception as exc:
            self.logger.error("Provider failed for %s: %s. Attempting fallback.", code, exc)
            if cached_df is not None and not cached_df.empty:
                return cached_df
            return pd.DataFrame()

        if not self.validator.validate(raw_df, provider_symbol):
            self.logger.error("Data validation failed for %s.", code)
            return pd.DataFrame()

        return self.cache.merge_and_save(code, cached_df, raw_df)

    @staticmethod
    def _provider_symbol(symbol: str, market: str) -> str:
        suffix = _MARKET_SUFFIX.get(market.upper())
        if suffix:
            return f"{symbol}.{suffix}"
        return symbol
