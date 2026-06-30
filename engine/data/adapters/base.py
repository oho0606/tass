from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date
from typing import Protocol

import pandas as pd


class BaseMarketDataAdapter(ABC):
    """Yahoo, KIS, Kiwoom adapters implement this interface."""

    @abstractmethod
    def fetch_ohlcv(
        self,
        symbol: str,
        market: str,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:
        pass


class DataAdapter(Protocol):
    def fetch_ohlcv(self, symbol: str, start: date, end: date) -> pd.DataFrame: ...

    def to_yahoo_symbol(self, symbol: str, market: str = "KS") -> str: ...


ADAPTER_REGISTRY: dict[str, type] = {}


def register_adapter(name: str):
    def decorator(cls):
        ADAPTER_REGISTRY[name] = cls
        return cls

    return decorator


def get_adapter(name: str, **kwargs) -> DataAdapter:
    if name not in ADAPTER_REGISTRY:
        raise ValueError(f"Unknown adapter: {name}. Available: {list(ADAPTER_REGISTRY)}")
    return ADAPTER_REGISTRY[name](**kwargs)
