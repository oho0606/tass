"""Load cached or live KOSPI/KOSDAQ OHLCV for backtests and pipelines."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from engine.core.logging import get_logger
from engine.data.engine import DataEngine, DataEngineConfig
from engine.data.universe import UniverseEntry, load_universe
from engine.data.validator import validate_ohlcv
from engine.indicators.registry import compute_all

logger = get_logger(__name__)


@dataclass(frozen=True)
class MarketDataLoadResult:
    """OHLCV frames loaded for a universe."""

    ohlcv_by_symbol: dict[str, pd.DataFrame]
    skipped_symbols: tuple[str, ...] = ()
    data_source: str = "cache"
    lookback_days: int = 0
    universe_path: Path | None = None


def load_universe_ohlcv(
    universe_path: Path,
    *,
    lookback_days: int = 3650,
    use_cache: bool = True,
    fetch_missing: bool = True,
    min_bars: int = 60,
    cache_dir: Path | None = None,
    adapter: str = "yahoo",
    compute_indicators: bool = False,
) -> MarketDataLoadResult:
    """Load OHLCV for all symbols in a universe CSV.

    Uses ``data/cache`` parquet files when available. Missing symbols are fetched
    from the configured adapter when ``fetch_missing`` is True.
    """
    entries = load_universe(universe_path)
    if not entries:
        return MarketDataLoadResult(ohlcv_by_symbol={}, universe_path=universe_path)

    end = date.today()
    start = end - timedelta(days=lookback_days)
    engine = DataEngine(
        DataEngineConfig(
            adapter_name=adapter,
            min_bars=min_bars,
            cache_dir=cache_dir or Path("data/cache"),
        )
    )

    frames: dict[str, pd.DataFrame] = {}
    skipped: list[str] = []
    used_cache_only = True

    for entry in entries:
        yahoo_sym = engine.adapter.to_yahoo_symbol(entry.symbol, entry.market)
        cached = engine.store.load(yahoo_sym) if use_cache else None
        if cached is not None and len(cached) >= min_bars:
            subset = cached.loc[str(start) : str(end)]
            if len(subset) >= min_bars:
                df = subset.copy()
            else:
                df = cached.copy()
        elif fetch_missing:
            used_cache_only = False
            df, validation = engine.get_ohlcv(
                yahoo_sym,
                start=start,
                end=end,
                use_cache=use_cache,
            )
            if df.empty or not validation.valid:
                logger.warning("Skipping {} — no valid OHLCV", entry.symbol)
                skipped.append(entry.symbol)
                continue
        else:
            logger.warning("Skipping {} — cache miss and fetch disabled", entry.symbol)
            skipped.append(entry.symbol)
            continue

        if compute_indicators:
            df = compute_all(df)
        frames[entry.symbol] = df

    source = "cache" if used_cache_only and use_cache else "yahoo"
    if skipped and frames:
        source = f"{source}+partial"
    if not frames and skipped:
        source = "unavailable"

    return MarketDataLoadResult(
        ohlcv_by_symbol=frames,
        skipped_symbols=tuple(skipped),
        data_source=source,
        lookback_days=lookback_days,
        universe_path=universe_path,
    )


def prefetch_universe_cache(
    universe_path: Path,
    *,
    lookback_days: int = 3650,
    min_bars: int = 60,
    cache_dir: Path | None = None,
    adapter: str = "yahoo",
) -> MarketDataLoadResult:
    """Fetch and persist OHLCV for all universe symbols."""
    return load_universe_ohlcv(
        universe_path,
        lookback_days=lookback_days,
        use_cache=True,
        fetch_missing=True,
        min_bars=min_bars,
        cache_dir=cache_dir,
        adapter=adapter,
        compute_indicators=False,
    )


def build_market_cache(
    universe_path: Path,
    *,
    start_date: str = "2020-01-01",
    cache_dir: Path | None = None,
    adapter: str = "yahoo",
    min_bars: int = 120,
    incremental: bool = True,
) -> MarketDataLoadResult:
    """전체 Universe OHLCV 캐시 구축 및 Incremental Update."""
    from datetime import date

    entries = load_universe(universe_path)
    if not entries:
        return MarketDataLoadResult(ohlcv_by_symbol={}, universe_path=universe_path)

    end = date.today()
    start = date.fromisoformat(start_date)
    engine = DataEngine(
        DataEngineConfig(
            adapter_name=adapter,
            min_bars=min_bars,
            cache_dir=cache_dir or Path("data/cache"),
        )
    )

    frames: dict[str, pd.DataFrame] = {}
    skipped: list[str] = []

    for entry in entries:
        if incremental:
            df = engine.update_cache(entry.symbol, entry.market, start, end)
        else:
            yahoo_sym = engine.adapter.to_yahoo_symbol(entry.symbol, entry.market)
            df = engine.adapter.fetch_ohlcv(
                entry.symbol,
                entry.market,
                start.isoformat(),
                end.isoformat(),
            )
            if not df.empty:
                engine.store.save(yahoo_sym, df)

        validation = validate_ohlcv(df, min_bars=min_bars)
        if df.empty or not validation.valid:
            logger.warning("Skipping {} — cache build failed validation", entry.symbol)
            skipped.append(entry.symbol)
            continue
        frames[entry.symbol] = df

    source = "cache+incremental" if incremental else "yahoo"
    if skipped and frames:
        source = f"{source}+partial"
    if not frames and skipped:
        source = "unavailable"

    return MarketDataLoadResult(
        ohlcv_by_symbol=frames,
        skipped_symbols=tuple(skipped),
        data_source=source,
        lookback_days=(end - start).days,
        universe_path=universe_path,
    )
