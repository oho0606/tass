from __future__ import annotations

import logging
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from engine.data.adapters.base import BaseMarketDataAdapter, register_adapter
from engine.data.providers.yahoo_provider import YahooFinanceProvider
from engine.data.store import ParquetStore
from engine.data.validators import DataQualityValidator

_OHLCV_COLUMNS = ("open", "high", "low", "close", "volume")


@register_adapter("yahoo")
class YahooAdapter(BaseMarketDataAdapter):
    """Legacy adapter registry wrapper delegating OHLCV fetch to YahooFinanceProvider."""

    def __init__(
        self,
        max_retries: int = 3,
        retry_delay: int = 3,
        cache_dir: Path | str | None = None,
        min_rows: int = 120,
    ):
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.cache_dir = Path(cache_dir or "data/cache")
        self.logger = logging.getLogger("YahooAdapter")
        self.validator = DataQualityValidator(min_rows=min_rows)
        self.store = ParquetStore(self.cache_dir)
        self._provider = YahooFinanceProvider()

    def to_yahoo_symbol(self, symbol: str, market: str = "KS") -> str:
        code = symbol.strip().split(".")[0].zfill(6)
        suffix = "KQ" if market.upper() in ("KQ", "KOSDAQ") else "KS"
        return f"{code}.{suffix}"

    def _load_fallback_cache(self, symbol: str) -> pd.DataFrame:
        cached = self.store.load(symbol)
        if cached is not None and not cached.empty:
            self.logger.info("[%s] Using cached fallback data.", symbol)
            return cached
        return pd.DataFrame(columns=list(_OHLCV_COLUMNS))

    def fetch_ohlcv(
        self,
        symbol: str,
        market: str | date = "KS",
        start_date: str | date | None = None,
        end_date: str | date | None = None,
    ) -> pd.DataFrame:
        """Fetch OHLCV. Accepts legacy (symbol, start, end) or spec (code, market, dates)."""
        if isinstance(market, date):
            start = market
            end = start_date if isinstance(start_date, date) else date.today()
            yahoo_sym = (
                symbol
                if ("." in symbol or symbol.startswith("^"))
                else self.to_yahoo_symbol(symbol)
            )
            return self._fetch_with_fallback(yahoo_sym, start, end)

        code = symbol.strip().split(".")[0].zfill(6)
        yahoo_sym = self.to_yahoo_symbol(code, str(market))
        start = pd.to_datetime(start_date).date() if start_date else date.today() - timedelta(days=400)
        end = pd.to_datetime(end_date).date() if end_date else date.today()
        return self._fetch_with_fallback(yahoo_sym, start, end, fallback_symbol=yahoo_sym)

    def _fetch_with_fallback(
        self,
        yahoo_sym: str,
        start: date,
        end: date,
        *,
        fallback_symbol: str | None = None,
    ) -> pd.DataFrame:
        fallback_symbol = fallback_symbol or yahoo_sym
        try:
            df = self._provider.fetch_ohlcv(
                yahoo_sym,
                start.isoformat(),
                end.isoformat(),
            )
            if self.validator.validate(df, yahoo_sym):
                return df
            self.logger.warning("[%s] Validation failed after provider fetch.", yahoo_sym)
        except Exception as exc:
            self.logger.error("[%s] Provider error: %s", yahoo_sym, exc)

        self.logger.error("[%s] Fetch failed. Attempting cache fallback...", yahoo_sym)
        return self._load_fallback_cache(fallback_symbol)
