#!/usr/bin/env python3
"""Prefetch KOSPI/KOSDAQ OHLCV into data/cache for offline backtests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from config.app_settings import get_settings
from engine.application.market_data_loader import build_market_cache, prefetch_universe_cache
from engine.core.logging import setup_logging


def main() -> int:
    parser = argparse.ArgumentParser(description="Cache KRX OHLCV for TASS backtests")
    parser.add_argument(
        "--universe",
        type=Path,
        default=Path("config/universe_krx_backtest.csv"),
        help="Universe CSV path",
    )
    parser.add_argument(
        "--start-date",
        default="2020-01-01",
        help="History start date for full cache build (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=3650,
        help="History window to fetch (~10 years default) for legacy prefetch mode",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("data/cache"),
        help="Parquet cache directory",
    )
    parser.add_argument(
        "--adapter",
        default="yahoo",
        help="Data adapter name",
    )
    parser.add_argument(
        "--min-bars",
        type=int,
        default=120,
        help="Minimum valid OHLCV bars required per symbol",
    )
    parser.add_argument(
        "--full-rebuild",
        action="store_true",
        help="Ignore cache and fetch full history from --start-date",
    )
    parser.add_argument(
        "--legacy-prefetch",
        action="store_true",
        help="Use lookback-days prefetch instead of build_market_cache",
    )
    args = parser.parse_args()

    app_settings = get_settings()
    setup_logging(log_level=app_settings.log_level, log_dir=app_settings.log_dir)

    if args.legacy_prefetch:
        result = prefetch_universe_cache(
            args.universe,
            lookback_days=args.lookback_days,
            min_bars=args.min_bars,
            cache_dir=args.cache_dir,
            adapter=args.adapter,
        )
    else:
        result = build_market_cache(
            args.universe,
            start_date=args.start_date,
            cache_dir=args.cache_dir,
            adapter=args.adapter,
            min_bars=args.min_bars,
            incremental=not args.full_rebuild,
        )

    summary = {
        "universe": str(args.universe),
        "loaded": sorted(result.ohlcv_by_symbol.keys()),
        "skipped": list(result.skipped_symbols),
        "data_source": result.data_source,
        "lookback_days": result.lookback_days,
        "cache_dir": str(args.cache_dir),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if result.ohlcv_by_symbol else 1


if __name__ == "__main__":
    raise SystemExit(main())
