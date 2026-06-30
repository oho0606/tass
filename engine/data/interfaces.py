from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List

import pandas as pd


class IDataProvider(ABC):
    """OHLCV data provider interface (Yahoo, KIS, Kiwoom)."""

    @abstractmethod
    def fetch_ohlcv(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        pass


class IMetaDataProvider(ABC):
    """Market, index, and universe metadata provider (PyKRX)."""

    @abstractmethod
    def get_universe(self, market: str, date: str) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    def get_index_ohlcv(self, index_name: str, start_date: str, end_date: str) -> pd.DataFrame:
        pass
