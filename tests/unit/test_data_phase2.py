"""Phase 2 tests: KIS provider, fallback chain, DataEngine pipeline integration."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from engine.data.engine import DataEngine, DataEngineConfig, _parse_krx_symbol
from engine.data.providers.kis_client import KISClient, KISConfig
from engine.data.providers.kis_provider import KISProvider
from engine.data.providers.yahoo_provider import YahooFinanceProvider
from engine.data.resilience import ProviderFallbackChain
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def _kis_row(day: str, base: float = 100.0) -> dict[str, str]:
    return {
        "stck_bsop_date": day,
        "stck_oprc": str(base),
        "stck_hgpr": str(base + 2),
        "stck_lwpr": str(base - 1),
        "stck_clpr": str(base + 1),
        "acml_vol": "1000000",
    }


def test_parse_krx_symbol_handles_suffixes() -> None:
    assert _parse_krx_symbol("005930.KS") == ("005930", "KS")
    assert _parse_krx_symbol("086520.KQ") == ("086520", "KQ")
    assert _parse_krx_symbol("^KS11") is None


def test_kis_provider_normalizes_rows() -> None:
    config = KISConfig(app_key="key", app_secret="secret")
    client = MagicMock(spec=KISClient)
    client.get_daily_ohlcv.return_value = [
        _kis_row("20240102", 100),
        _kis_row("20240103", 101),
    ]
    provider = KISProvider(config=config, client=client)

    df = provider.fetch_ohlcv("005930", "2024-01-01", "2024-01-10")
    assert list(df.columns) == ["open", "high", "low", "close", "volume"]
    assert len(df) == 2
    assert float(df.iloc[-1]["close"]) == 102.0


def test_kis_client_paginates_when_api_returns_full_page() -> None:
    config = KISConfig(app_key="key", app_secret="secret")
    client = KISClient(config)
    first_page = [_kis_row("20240102", 100 + i) for i in range(100)]
    second_page = [_kis_row("20231228", 98)]

    with patch.object(client, "_request_daily_chart", side_effect=[first_page, second_page]):
        rows = client.get_daily_ohlcv("005930", date(2023, 12, 20), date(2024, 6, 1))

    assert len(rows) == 101


def test_provider_fallback_chain_uses_secondary_after_threshold() -> None:
    primary = MagicMock()
    fallback = MagicMock()
    primary.fetch_ohlcv.side_effect = RuntimeError("kis down")
    fallback.fetch_ohlcv.return_value = make_uptrend_ohlcv(n=150)

    chain = ProviderFallbackChain(primary, fallback, failure_threshold=1)
    df = chain.fetch_ohlcv("005930.KS", "2024-01-01", "2024-06-01")

    assert len(df) == 150
    fallback.fetch_ohlcv.assert_called_once()


def test_data_engine_get_ohlcv_uses_pipeline_for_krx_symbol(tmp_path: Path) -> None:
    engine = DataEngine(
        DataEngineConfig(min_bars=60, cache_dir=tmp_path, adapter_name="yahoo")
    )
    cached = make_uptrend_ohlcv(n=150)
    engine.pipeline.cache.store.save("005930", cached)
    start = pd.to_datetime(cached.index.min()).date()
    end = pd.to_datetime(cached.index.max()).date()

    with patch.object(engine.pipeline.ohlcv_provider, "fetch_ohlcv") as fetch_mock:
        df, validation = engine.get_ohlcv("005930.KS", start=start, end=end, use_cache=True)

    fetch_mock.assert_not_called()
    assert validation.valid is True
    assert len(df) >= 60


def test_kis_provider_requires_credentials() -> None:
    config = KISConfig(app_key="", app_secret="")
    with pytest.raises(ValueError, match="not configured"):
        KISProvider(config=config)
