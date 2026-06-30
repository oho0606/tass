"""Unit tests for OHLCV sanitize and cache validation."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from engine.data.validator import sanitize_ohlcv, validate_ohlcv
from scripts.validate_cache import validate_universe_cache
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def test_sanitize_ohlcv_fixes_split_adjusted_row():
    df = make_uptrend_ohlcv(n=80)
    df.loc[df.index[10], "open"] = 200.0
    df.loc[df.index[10], "close"] = 198.0
    df.loc[df.index[10], "high"] = 195.0
    df.loc[df.index[10], "low"] = 190.0

    before = validate_ohlcv(df, min_bars=60)
    assert not before.valid

    fixed = sanitize_ohlcv(df)
    after = validate_ohlcv(fixed, min_bars=60)
    assert after.valid
    assert fixed.loc[fixed.index[10], "high"] >= fixed.loc[fixed.index[10], "open"]


@pytest.fixture
def cache_setup(tmp_path: Path):
    universe = tmp_path / "universe.csv"
    universe.write_text("symbol,name,market\n005930,삼성전자,KS\n", encoding="utf-8")
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()
    df = make_uptrend_ohlcv(n=100)
    df.to_parquet(cache_dir / "005930.parquet")
    return universe, cache_dir


def test_validate_cache_passes(cache_setup):
    universe, cache_dir = cache_setup
    report = validate_universe_cache(universe, cache_dir, min_bars=60)
    assert report["passed"] is True
    assert report["valid_count"] == 1


def test_validate_cache_detects_missing(cache_setup):
    universe, cache_dir = cache_setup
    (cache_dir / "005930.parquet").unlink()
    report = validate_universe_cache(universe, cache_dir, min_bars=60)
    assert report["passed"] is False
    assert "005930" in report["missing"]


def test_validate_cache_repair(tmp_path: Path):
    universe = tmp_path / "universe.csv"
    universe.write_text("symbol,name,market\n005930,삼성전자,KS\n", encoding="utf-8")
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()
    df = make_uptrend_ohlcv(n=100)
    df.loc[df.index[5], "open"] = 300.0
    df.loc[df.index[5], "high"] = 290.0
    df.to_parquet(cache_dir / "005930.parquet")

    report = validate_universe_cache(universe, cache_dir, min_bars=60, repair=True)
    assert report["passed"] is True
    assert "005930" in report["repaired"]
