from __future__ import annotations

import logging
from datetime import date, timedelta
from typing import Dict, List

import pandas as pd

from engine.data.interfaces import IMetaDataProvider

_INDEX_CODES = {
    "KOSPI": "1001",
    "KOSDAQ": "2001",
    "^KS11": "1001",
    "^KQ11": "2001",
}

_MARKET_ALIASES = {
    "KS": "KOSPI",
    "KQ": "KOSDAQ",
    "KOSPI": "KOSPI",
    "KOSDAQ": "KOSDAQ",
}

_OHLCV_COLUMNS = ("open", "high", "low", "close", "volume")


class PyKRXProvider(IMetaDataProvider):
    """PyKRX-backed universe and index metadata provider."""

    def __init__(self) -> None:
        self.logger = logging.getLogger("PyKRXProvider")

    def get_universe(self, market: str, date: str) -> List[Dict[str, str]]:
        from pykrx import stock

        resolved_market = _MARKET_ALIASES.get(market.upper(), market.upper())
        target_date = date.strip() or None
        as_of = self._resolve_trading_date(target_date, stock)

        tickers = stock.get_market_ticker_list(as_of, market=resolved_market)
        sector_map = self._load_sector_map(stock, as_of, resolved_market)

        universe: list[dict[str, str]] = []
        for ticker in tickers:
            code = str(ticker).zfill(6)
            name = stock.get_market_ticker_name(ticker, as_of)
            universe.append(
                {
                    "code": code,
                    "name": name,
                    "market": resolved_market,
                    "sector": sector_map.get(code, ""),
                }
            )
        return universe

    def get_index_ohlcv(self, index_name: str, start_date: str, end_date: str) -> pd.DataFrame:
        from pykrx import stock

        index_code = _INDEX_CODES.get(index_name.upper(), index_name)
        start = pd.to_datetime(start_date).strftime("%Y%m%d")
        end = pd.to_datetime(end_date).strftime("%Y%m%d")

        raw = stock.get_index_ohlcv_by_date(start, end, index_code)
        if raw is None or raw.empty:
            self.logger.warning("No index OHLCV for %s (%s)", index_name, index_code)
            return pd.DataFrame(columns=list(_OHLCV_COLUMNS))

        df = raw.rename(
            columns={
                "시가": "open",
                "고가": "high",
                "저가": "low",
                "종가": "close",
                "거래량": "volume",
            }
        )
        df.index = pd.to_datetime(df.index)
        df.index.name = "date"
        return df[list(_OHLCV_COLUMNS)].dropna()

    def _resolve_trading_date(self, target_date: str | None, stock_module) -> str:
        if target_date:
            return pd.to_datetime(target_date).strftime("%Y%m%d")

        probe = date.today()
        for _ in range(10):
            as_of = probe.strftime("%Y%m%d")
            try:
                tickers = stock_module.get_market_ticker_list(as_of, market="KOSPI")
                if tickers:
                    return as_of
            except Exception:
                pass
            probe -= timedelta(days=1)

        return date.today().strftime("%Y%m%d")

    def _load_sector_map(self, stock_module, as_of: str, market: str) -> dict[str, str]:
        try:
            sectors = stock_module.get_market_sector_classifications(as_of, market)
        except Exception as exc:
            self.logger.debug("Sector lookup unavailable for %s: %s", market, exc)
            return {}

        if sectors is None or sectors.empty:
            return {}

        code_col = "종목코드" if "종목코드" in sectors.columns else sectors.columns[0]
        sector_col = "업종명" if "업종명" in sectors.columns else sectors.columns[-1]
        return {
            str(row[code_col]).zfill(6): str(row[sector_col])
            for _, row in sectors.iterrows()
        }
