"""Unit tests for Data Layer v2.0 pipeline, cache, and providers."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest

from engine.data.cache.manager import CacheManager
from engine.data.pipeline import DataPipeline
from engine.data.providers.yahoo_provider import YahooFinanceProvider
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def test_cache_manager_is_up_to_date(tmp_path: Path) -> None:
    cache = CacheManager(tmp_path)
    df = make_uptrend_ohlcv(n=10)
    cache.store.save("005930", df)

    loaded = cache.load("005930")
    last_date = pd.to_datetime(loaded.index.max()).date()
    assert cache.is_up_to_date(loaded, last_date.isoformat()) is True
    assert cache.is_up_to_date(loaded, "2099-12-31") is False
    assert cache.is_up_to_date(None, "2026-01-01") is False


def test_cache_manager_merge_and_save_deduplicates(tmp_path: Path) -> None:
    cache = CacheManager(tmp_path)
    base = make_uptrend_ohlcv(n=10)
    overlap = make_uptrend_ohlcv(n=5)
    overlap.index = base.index[-5:]

    merged = cache.merge_and_save("005930", base, overlap)
    assert len(merged) == len(base)
    assert not merged.index.duplicated().any()


def test_yahoo_provider_raises_on_empty_download() -> None:
    provider = YahooFinanceProvider()
    with patch("engine.data.providers.yahoo_provider.yf.download", return_value=pd.DataFrame()):
        with pytest.raises(ValueError, match="Empty Data"):
            provider.fetch_ohlcv("005930.KS", "2024-01-01", "2024-06-01")


def test_data_pipeline_returns_cached_when_up_to_date(tmp_path: Path) -> None:
    pipeline = DataPipeline(cache_dir=tmp_path, min_rows=60)
    cached = make_uptrend_ohlcv(n=150)
    pipeline.cache.store.save("005930", cached)

    with patch.object(pipeline.ohlcv_provider, "fetch_ohlcv") as fetch_mock:
        result = pipeline.get_validated_data(
            "005930",
            "KOSPI",
            "2024-01-01",
            pd.to_datetime(cached.index.max()).date().isoformat(),
        )

    fetch_mock.assert_not_called()
    assert len(result) == len(cached)


def test_data_pipeline_falls_back_to_cache_on_provider_failure(tmp_path: Path) -> None:
    pipeline = DataPipeline(cache_dir=tmp_path, min_rows=60)
    cached = make_uptrend_ohlcv(n=150)
    pipeline.cache.store.save("005930", cached)

    with patch.object(
        pipeline.ohlcv_provider,
        "fetch_ohlcv",
        side_effect=ConnectionError("network down"),
    ):
        result = pipeline.get_validated_data(
            "005930",
            "KOSPI",
            "2024-01-01",
            date.today().isoformat(),
        )

    assert len(result) == len(cached)


def test_data_pipeline_fetches_and_persists_when_cache_stale(tmp_path: Path) -> None:
    pipeline = DataPipeline(cache_dir=tmp_path, min_rows=60)
    stale = make_uptrend_ohlcv(n=150)
    pipeline.cache.store.save("005930", stale)

    fresh = make_uptrend_ohlcv(n=160)
    with patch.object(pipeline.ohlcv_provider, "fetch_ohlcv", return_value=fresh):
        result = pipeline.get_validated_data(
            "005930",
            "KOSPI",
            "2024-01-01",
            date.today().isoformat(),
        )

    assert len(result) >= len(stale)
    reloaded = pipeline.cache.load("005930")
    assert reloaded is not None
    assert len(reloaded) == len(result)


def test_pykrx_provider_get_universe_shape() -> None:
    from engine.data.providers.pykrx_provider import PyKRXProvider

    provider = PyKRXProvider()
    with patch("pykrx.stock.get_market_ticker_list", return_value=["005930", "000660"]):
        with patch("pykrx.stock.get_market_ticker_name", side_effect=["삼성전자", "SK하이닉스"]):
            with patch(
                "pykrx.stock.get_market_sector_classifications",
                return_value=pd.DataFrame(),
            ):
                universe = provider.get_universe("KOSPI", "20240619")

    assert len(universe) == 2
    assert universe[0]["code"] == "005930"
    assert universe[0]["market"] == "KOSPI"
    assert "name" in universe[0]


def test_generate_universe_csv_writes_expected_columns(tmp_path: Path) -> None:
    from engine.data.providers.pykrx_provider import PyKRXProvider
    from engine.data.universe import generate_universe_csv, load_universe

    provider = PyKRXProvider()
    with patch("pykrx.stock.get_market_ticker_list", return_value=["005930"]):
        with patch("pykrx.stock.get_market_ticker_name", return_value="삼성전자"):
            with patch(
                "pykrx.stock.get_market_sector_classifications",
                return_value=pd.DataFrame(),
            ):
                output = generate_universe_csv(
                    tmp_path / "universe.csv",
                    markets=("KOSPI",),
                    target_date="20240619",
                    meta_provider=provider,
                )

    entries = load_universe(output)
    assert len(entries) == 1
    assert entries[0].symbol == "005930"
    assert entries[0].market == "KS"
