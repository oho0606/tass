"""Stock data helpers for API (indicators, metadata)."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from api.schemas.stock import IndicatorBar, IndicatorsResponse, StockMetaResponse
from api.services.state import TassApiState
from engine.application.settings import load_pipeline_settings
from engine.core.exceptions import DataException
from engine.data.engine import DataEngine
from engine.data.universe import load_universe
from engine.indicators.registry import compute_all


def _safe_float(value) -> float | None:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def get_stock_meta(state: TassApiState, symbol: str) -> StockMetaResponse:
    pick = state.get_pick(symbol)
    if pick is None:
        name = _lookup_name(state, symbol)
        if name is None:
            raise DataException(f"Stock not found: {symbol}", context={"symbol": symbol})
        return StockMetaResponse(symbol=symbol, name=name)
    return StockMetaResponse(
        symbol=pick.symbol,
        name=pick.name,
        rank=pick.rank,
        total_score=pick.total_score,
        max_score=pick.max_score,
        grade=pick.grade,
        recommendation=pick.recommendation,
        gate=pick.gate,
    )


def get_indicators(state: TassApiState, symbol: str, *, limit: int = 120) -> IndicatorsResponse:
    settings = state.settings
    universe_path = Path("config/universe_sample.csv")
    entry = _lookup_entry(universe_path, symbol)
    if entry is None:
        raise DataException(f"Stock not in universe: {symbol}", context={"symbol": symbol})

    data_engine = DataEngine(settings.to_data_engine_config())
    yahoo_sym = data_engine.adapter.to_yahoo_symbol(entry.symbol, entry.market)
    df, _validation = data_engine.get_ohlcv(yahoo_sym, use_cache=True)
    if df.empty:
        raise DataException(f"No OHLCV data for {symbol}", context={"symbol": symbol})

    df = compute_all(df).tail(limit)
    bars: list[IndicatorBar] = []
    for idx, row in df.iterrows():
        date_str = idx.strftime("%Y-%m-%d") if hasattr(idx, "strftime") else str(idx)[:10]
        bars.append(
            IndicatorBar(
                date=date_str,
                open=float(row["open"]),
                high=float(row["high"]),
                low=float(row["low"]),
                close=float(row["close"]),
                volume=float(row["volume"]),
                sma_20=_safe_float(row.get("sma_20")),
                sma_60=_safe_float(row.get("sma_60")),
                macd=_safe_float(row.get("macd")),
                macd_signal=_safe_float(row.get("macd_signal")),
                macd_hist=_safe_float(row.get("macd_hist")),
                atr=_safe_float(row.get("atr")),
            )
        )

    pick = state.get_pick(symbol)
    name = pick.name if pick else entry.name
    return IndicatorsResponse(
        symbol=symbol,
        name=name,
        bars=bars,
        meta={"bar_count": len(bars), "adapter": settings.adapter},
    )


def _lookup_entry(universe_path: Path, symbol: str):
    if not universe_path.exists():
        return None
    for entry in load_universe(universe_path):
        if entry.symbol == symbol.strip():
            return entry
    return None


def _lookup_name(state: TassApiState, symbol: str) -> str | None:
    entry = _lookup_entry(Path("config/universe_sample.csv"), symbol)
    return entry.name if entry else None
