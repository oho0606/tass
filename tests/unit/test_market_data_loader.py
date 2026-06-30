"""Unit tests for KRX market data loader."""

from __future__ import annotations

from pathlib import Path

from engine.application.market_data_loader import load_universe_ohlcv
from tests.fixtures.market_cache import seed_krx_cache


def test_cache_only_load_skips_missing_symbols(tmp_path: Path) -> None:
    seed_krx_cache(tmp_path, bars=120)
    result = load_universe_ohlcv(
        Path("tests/fixtures/universe_krx_mini.csv"),
        lookback_days=200,
        use_cache=True,
        fetch_missing=False,
        cache_dir=tmp_path,
    )
    assert "005930" in result.ohlcv_by_symbol
    assert "086520" in result.ohlcv_by_symbol
    assert result.skipped_symbols == ()
    assert result.data_source == "cache"
