from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from engine.data.engine import DataEngine
from engine.gate.config import load_gate_pipeline_yaml

DEFAULT_KOSPI_SYMBOL = "^KS11"
DEFAULT_KOSDAQ_SYMBOL = "^KQ11"


def worst_market_trend(*trends: str) -> str:
    """Return the most pessimistic market trend state."""
    priority = {"CRASH": 0, "DOWN": 1, "UP": 2}
    normalized = [trend if trend in priority else "UP" for trend in trends]
    return min(normalized, key=lambda trend: priority[trend])


def normalize_listing_market(market: str | None) -> str:
    """Normalize universe market codes to KS or KQ."""
    normalized = (market or "KS").strip().upper()
    if normalized in {"KQ", "KOSDAQ"}:
        return "KQ"
    return "KS"


def resolve_effective_market_trend(
    *,
    kospi_trend: str,
    kosdaq_trend: str,
    listing_market: str | None = None,
    combine_mode: str = "worst",
    market_trend: str | None = None,
) -> str:
    """Resolve the market trend used by Market Gate for one symbol."""
    mode = (combine_mode or "worst").strip().lower()
    if mode == "listing":
        if normalize_listing_market(listing_market) == "KQ":
            return kosdaq_trend
        return kospi_trend

    if market_trend is not None:
        return market_trend
    return worst_market_trend(kospi_trend, kosdaq_trend)


def classify_index_trend(
    df: pd.DataFrame,
    *,
    crash_drawdown: float = 0.08,
) -> str:
    """Classify index trend from OHLCV using SMA20/SMA60 and drawdown."""
    if df.empty or len(df) < 60 or "close" not in df.columns:
        return "UP"

    close = df["close"]
    last = float(close.iloc[-1])
    sma20 = float(close.rolling(20).mean().iloc[-1])
    sma60 = float(close.rolling(60).mean().iloc[-1])
    peak_20 = float(close.iloc[-20:].max())

    if pd.isna(last) or pd.isna(sma20) or pd.isna(sma60):
        return "UP"

    drawdown = (peak_20 - last) / peak_20 if peak_20 > 0 else 0.0
    if drawdown >= crash_drawdown and last < sma60:
        return "CRASH"
    if last < sma20 or sma20 < sma60:
        return "DOWN"
    return "UP"


def load_market_context(
    data_engine: DataEngine,
    *,
    use_cache: bool = True,
    pipeline_config_path: Path | None = None,
) -> dict[str, Any]:
    """Fetch KOSPI/KOSDAQ indices and build gate pipeline market context."""
    gates = load_gate_pipeline_yaml(pipeline_config_path)
    market_config = gates.get("market") or {}

    kospi_symbol = market_config.get("kospi_symbol", DEFAULT_KOSPI_SYMBOL)
    kosdaq_symbol = market_config.get("kosdaq_symbol", DEFAULT_KOSDAQ_SYMBOL)
    crash_drawdown = float(market_config.get("crash_drawdown", 0.08))

    kospi_df, _ = data_engine.get_ohlcv(kospi_symbol, use_cache=use_cache)
    kosdaq_df, _ = data_engine.get_ohlcv(kosdaq_symbol, use_cache=use_cache)

    kospi_trend = classify_index_trend(kospi_df, crash_drawdown=crash_drawdown)
    kosdaq_trend = classify_index_trend(kosdaq_df, crash_drawdown=crash_drawdown)
    combined_trend = worst_market_trend(kospi_trend, kosdaq_trend)

    return {
        "kospi_trend": kospi_trend,
        "kosdaq_trend": kosdaq_trend,
        "market_trend": combined_trend,
    }
