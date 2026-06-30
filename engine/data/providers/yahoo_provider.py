from __future__ import annotations

import logging
from datetime import date, timedelta

import pandas as pd
import yfinance as yf
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from engine.data.interfaces import IDataProvider
from engine.data.validator import sanitize_ohlcv

_OHLCV_COLUMNS = ("open", "high", "low", "close", "volume")


class YahooFinanceProvider(IDataProvider):
    """Yahoo Finance OHLCV provider with exponential-backoff retries."""

    def __init__(self) -> None:
        self.logger = logging.getLogger("YahooProvider")

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type((ConnectionError, TimeoutError)),
        reraise=True,
    )
    def fetch_ohlcv(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        self.logger.info("Fetching %s via Yahoo Finance...", symbol)
        end = pd.to_datetime(end_date).date()
        df = yf.download(
            symbol,
            start=start_date,
            end=(end + timedelta(days=1)).isoformat(),
            progress=False,
            timeout=10,
            auto_adjust=True,
        )

        normalized = self._normalize(df)
        if normalized.empty:
            self.logger.warning("[%s] Returned empty dataframe.", symbol)
            raise ValueError("Empty Data")

        return normalized

    def _normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        if df is None or df.empty:
            return pd.DataFrame(columns=list(_OHLCV_COLUMNS))

        if isinstance(df.columns, pd.MultiIndex):
            df = df.copy()
            df.columns = df.columns.get_level_values(0)

        rename = {
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume",
        }
        df = df.rename(columns=rename)
        missing = [col for col in _OHLCV_COLUMNS if col not in df.columns]
        if missing:
            return pd.DataFrame(columns=list(_OHLCV_COLUMNS))

        out = df[list(_OHLCV_COLUMNS)].copy()
        out.index = pd.to_datetime(out.index).tz_localize(None)
        out.index.name = "date"
        out = out.dropna()
        return sanitize_ohlcv(out)
