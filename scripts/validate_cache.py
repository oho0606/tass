#!/usr/bin/env python3
"""Data Quality Gate — validate OHLCV cache completeness and integrity (Phase 6)."""

from __future__ import annotations

import argparse
import json
import time
import tracemalloc
from pathlib import Path

import pandas as pd

from config.app_settings import get_settings
from engine.application.settings import load_pipeline_settings
from engine.core.logging import setup_logging
from engine.data.universe import load_universe
from engine.data.validator import sanitize_ohlcv, validate_ohlcv


def _cache_path(cache_dir: Path, symbol: str) -> Path:
    return cache_dir / f"{symbol}.parquet"


def validate_universe_cache(
    universe_path: Path,
    cache_dir: Path,
    *,
    min_bars: int,
    repair: bool = False,
) -> dict:
    """Validate cached OHLCV for every symbol in universe."""
    universe = load_universe(universe_path)
    if not universe:
        return {"passed": False, "error": "empty_universe", "symbols": []}

    tracemalloc.start()
    start = time.perf_counter()

    missing: list[str] = []
    empty: list[str] = []
    invalid: list[dict] = []
    repaired: list[str] = []
    valid_symbols: list[str] = []

    for entry in universe:
        path = _cache_path(cache_dir, entry.symbol)
        if not path.exists():
            missing.append(entry.symbol)
            continue
        df = pd.read_parquet(path)
        if df.empty:
            empty.append(entry.symbol)
            continue

        if repair:
            fixed = sanitize_ohlcv(df)
            if not fixed.equals(df):
                fixed.to_parquet(path)
                df = fixed
                repaired.append(entry.symbol)

        result = validate_ohlcv(df, min_bars=min_bars)
        if not result.valid:
            invalid.append({"symbol": entry.symbol, "errors": result.errors})
            continue
        valid_symbols.append(entry.symbol)

    elapsed_ms = (time.perf_counter() - start) * 1000
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    passed = not missing and not empty and not invalid
    report = {
        "passed": passed,
        "universe": str(universe_path),
        "cache_dir": str(cache_dir),
        "total_symbols": len(universe),
        "valid_count": len(valid_symbols),
        "missing": missing,
        "empty": empty,
        "invalid": invalid,
        "load_elapsed_ms": round(elapsed_ms, 2),
        "peak_memory_mb": round(peak_bytes / (1024 * 1024), 2),
    }
    if repair:
        report["repaired"] = repaired
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate TASS market data cache")
    parser.add_argument("--universe", type=Path, default=Path("config/universe_sample.csv"))
    parser.add_argument("--cache-dir", type=Path, default=None)
    parser.add_argument("--min-bars", type=int, default=None)
    parser.add_argument("--repair", action="store_true", help="Sanitize and rewrite invalid OHLC rows")
    parser.add_argument("--output", type=Path, default=Path("output/cache_validation.json"))
    args = parser.parse_args()

    settings = get_settings()
    setup_logging(log_level=settings.log_level, log_dir=settings.log_dir)
    pipeline = load_pipeline_settings()
    cache_dir = args.cache_dir or pipeline.cache_dir
    min_bars = args.min_bars or pipeline.min_bars

    report = validate_universe_cache(
        args.universe,
        cache_dir,
        min_bars=min_bars,
        repair=args.repair,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report.get("passed") else 1


if __name__ == "__main__":
    raise SystemExit(main())
