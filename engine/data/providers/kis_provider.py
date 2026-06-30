from __future__ import annotations

import logging
from datetime import date

import pandas as pd
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from engine.data.interfaces import IDataProvider
from engine.data.providers.kis_client import KISClient, KISConfig

_OHLCV_COLUMNS = ("open", "high", "low", "close", "volume")


def load_kis_config() -> KISConfig:
    """Load KIS credentials from environment via AppSettings."""
    from config.app_settings import get_settings

    settings = get_settings()
    return KISConfig(
        app_key=settings.kis_app_key,
        app_secret=settings.kis_app_secret,
        base_url=settings.kis_base_url,
    )


class KISProvider(IDataProvider):
    """KIS Open API OHLCV provider with retry and standard TASS normalization."""

    def __init__(self, config: KISConfig | None = None, client: KISClient | None = None) -> None:
        self.logger = logging.getLogger("KISProvider")
        self.config = config or load_kis_config()
        if not self.config.is_configured:
            raise ValueError("KIS credentials are not configured (KIS_APP_KEY / KIS_APP_SECRET).")
        self.client = client or KISClient(self.config)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type((ConnectionError, TimeoutError)),
        reraise=True,
    )
    def fetch_ohlcv(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        code = symbol.strip().split(".")[0].zfill(6)
        start = pd.to_datetime(start_date).date()
        end = pd.to_datetime(end_date).date()
        self.logger.info("Fetching %s via KIS Open API...", code)

        rows = self.client.get_daily_ohlcv(code, start, end)
        normalized = self._normalize(rows)
        if normalized.empty:
            self.logger.warning("[%s] KIS returned empty dataframe.", code)
            raise ValueError("Empty Data")
        return normalized

    def _normalize(self, rows: list[dict]) -> pd.DataFrame:
        if not rows:
            return pd.DataFrame(columns=list(_OHLCV_COLUMNS))

        frame = pd.DataFrame(rows)
        frame["date"] = pd.to_datetime(frame["stck_bsop_date"], format="%Y%m%d")
        frame = frame.rename(
            columns={
                "stck_oprc": "open",
                "stck_hgpr": "high",
                "stck_lwpr": "low",
                "stck_clpr": "close",
                "acml_vol": "volume",
            }
        )
        for col in _OHLCV_COLUMNS:
            frame[col] = pd.to_numeric(frame[col], errors="coerce")

        out = frame.set_index("date")[list(_OHLCV_COLUMNS)].dropna()
        out.index = out.index.tz_localize(None)
        out.index.name = "date"
        return out.sort_index()
