from __future__ import annotations

import logging
import time

import pandas as pd

from engine.data.interfaces import IDataProvider

logger = logging.getLogger("ProviderFallbackChain")


class ProviderFallbackChain:
    """Primary provider with circuit-breaker style fallback to a secondary provider."""

    def __init__(
        self,
        primary: IDataProvider,
        fallback: IDataProvider | None = None,
        *,
        failure_threshold: int = 3,
        cooldown_seconds: int = 300,
    ) -> None:
        self.primary = primary
        self.fallback = fallback
        self.failure_threshold = failure_threshold
        self.cooldown_seconds = cooldown_seconds
        self._failure_count = 0
        self._circuit_open_until = 0.0

    def fetch_ohlcv(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        if self._circuit_open() and self.fallback is not None:
            logger.warning("Primary provider circuit open; using fallback for %s.", symbol)
            return self.fallback.fetch_ohlcv(symbol, start_date, end_date)

        try:
            df = self.primary.fetch_ohlcv(symbol, start_date, end_date)
            self._failure_count = 0
            return df
        except Exception as exc:
            self._failure_count += 1
            logger.error("Primary provider failed for %s (%s/%s): %s", symbol, self._failure_count, self.failure_threshold, exc)
            if self._failure_count >= self.failure_threshold:
                self._circuit_open_until = time.time() + self.cooldown_seconds
                logger.warning("Primary provider circuit opened for %ss.", self.cooldown_seconds)

            if self.fallback is not None:
                logger.info("Attempting fallback provider for %s.", symbol)
                return self.fallback.fetch_ohlcv(symbol, start_date, end_date)
            raise

    def _circuit_open(self) -> bool:
        if self._circuit_open_until <= 0:
            return False
        if time.time() >= self._circuit_open_until:
            self._circuit_open_until = 0.0
            self._failure_count = 0
            return False
        return True
