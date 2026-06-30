from __future__ import annotations

import logging
from datetime import date, timedelta

import pandas as pd

from engine.data.adapters.base import BaseMarketDataAdapter, register_adapter
from engine.data.providers.kis_provider import KISProvider
from engine.data.providers.yahoo_provider import YahooFinanceProvider
from engine.data.resilience import ProviderFallbackChain
from engine.data.store import ParquetStore
from engine.data.validators import DataQualityValidator

_OHLCV_COLUMNS = ("open", "high", "low", "close", "volume")


@register_adapter("kis")
class KISAdapter(BaseMarketDataAdapter):
    """KIS adapter registry wrapper with Yahoo fallback."""

    def __init__(
        self,
        max_retries: int = 3,
        retry_delay: int = 3,
        cache_dir: str | None = None,
        min_rows: int = 120,
        enable_fallback: bool = True,
        **kwargs,
    ):
        self.cache_dir = cache_dir or "data/cache"
        self.logger = logging.getLogger("KISAdapter")
        self.validator = DataQualityValidator(min_rows=min_rows)
        self.store = ParquetStore(self.cache_dir)
        yahoo = YahooFinanceProvider()
        try:
            primary = KISProvider()
            self._provider = (
                ProviderFallbackChain(primary, yahoo) if enable_fallback else primary
            )
        except ValueError:
            self._provider = yahoo

    def to_yahoo_symbol(self, symbol: str, market: str = "KS") -> str:
        code = symbol.strip().split(".")[0].zfill(6)
        suffix = "KQ" if market.upper() in ("KQ", "KOSDAQ") else "KS"
        return f"{code}.{suffix}"

    def fetch_ohlcv(
        self,
        symbol: str,
        market: str | date = "KS",
        start_date: str | date | None = None,
        end_date: str | date | None = None,
    ) -> pd.DataFrame:
        if isinstance(market, date):
            raise NotImplementedError("Use Yahoo adapter for legacy (symbol, start, end) calls.")

        code = symbol.strip().split(".")[0].zfill(6)
        provider_symbol = self.to_yahoo_symbol(code, str(market))
        start = pd.to_datetime(start_date).date() if start_date else date.today() - timedelta(days=400)
        end = pd.to_datetime(end_date).date() if end_date else date.today()
        return self._fetch_with_fallback(provider_symbol, start, end, fallback_symbol=provider_symbol)

    def _fetch_with_fallback(
        self,
        provider_symbol: str,
        start: date,
        end: date,
        *,
        fallback_symbol: str,
    ) -> pd.DataFrame:
        try:
            df = self._provider.fetch_ohlcv(
                provider_symbol,
                start.isoformat(),
                end.isoformat(),
            )
            if self.validator.validate(df, provider_symbol):
                return df
            self.logger.warning("[%s] Validation failed after provider fetch.", provider_symbol)
        except Exception as exc:
            self.logger.error("[%s] Provider error: %s", provider_symbol, exc)

        cached = self.store.load(fallback_symbol)
        if cached is not None and not cached.empty:
            return cached
        return pd.DataFrame(columns=list(_OHLCV_COLUMNS))


__all__ = ["KISAdapter"]
