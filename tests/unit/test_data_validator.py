"""Unit tests for DataQualityValidator and cache build helpers."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from engine.application.market_data_loader import build_market_cache
from engine.data.store import ParquetStore
from engine.data.validator import DataQualityValidator, validate_ohlcv
from tests.fixtures.market_cache import seed_krx_cache
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def test_data_quality_validator_accepts_valid_frame() -> None:
    df = make_uptrend_ohlcv(n=150)
    assert DataQualityValidator(min_rows=120).validate(df, "005930.KS") is True


def test_data_quality_validator_rejects_short_history() -> None:
    df = make_uptrend_ohlcv(n=80)
    assert DataQualityValidator(min_rows=120).validate(df, "005930.KS") is False


def test_data_quality_validator_rejects_invalid_ohlc() -> None:
    df = make_uptrend_ohlcv(n=150)
    df.loc[df.index[0], "low"] = df.loc[df.index[0], "high"] + 1
    assert DataQualityValidator(min_rows=120).validate(df, "005930.KS") is False


def test_validate_ohlcv_reports_duplicated_dates() -> None:
    df = make_uptrend_ohlcv(n=150)
    dup = df.iloc[[0]].copy()
    dup.index = [df.index[0]]
    merged = pd.concat([df, dup]).sort_index()
    result = validate_ohlcv(merged, min_bars=60)
    assert result.valid is False
    assert "duplicated_dates" in result.errors


def test_parquet_store_merge_and_save_deduplicates(tmp_path: Path) -> None:
    store = ParquetStore(tmp_path)

    base = make_uptrend_ohlcv(n=10)
    overlap = make_uptrend_ohlcv(n=5)
    overlap.index = base.index[-5:]
    store.merge_and_save("005930.KS", base)
    merged = store.merge_and_save("005930.KS", overlap)
    assert len(merged) == len(base)
    assert not merged.index.duplicated().any()


def test_build_market_cache_uses_existing_cache(tmp_path: Path) -> None:
    seed_krx_cache(tmp_path, bars=150)
    result = build_market_cache(
        Path("tests/fixtures/universe_krx_mini.csv"),
        start_date="2020-01-01",
        cache_dir=tmp_path,
        min_bars=120,
        incremental=True,
    )
    assert "005930" in result.ohlcv_by_symbol
    assert "086520" in result.ohlcv_by_symbol
    assert result.skipped_symbols == ()
