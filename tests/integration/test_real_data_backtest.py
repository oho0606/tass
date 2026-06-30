"""Integration tests for KRX cached OHLCV backtests."""

from __future__ import annotations

from pathlib import Path

import pytest

from engine.application import BacktestService
from tests.fixtures.market_cache import seed_krx_cache


@pytest.fixture
def krx_cache_dir(tmp_path: Path) -> Path:
    seed_krx_cache(tmp_path, bars=400)
    return tmp_path


def test_load_cached_krx_universe(krx_cache_dir: Path) -> None:
    service = BacktestService()
    universe = Path("tests/fixtures/universe_krx_mini.csv")
    market_data = service.load_market_data(
        universe,
        use_cache=True,
        fetch_missing=False,
        cache_dir=krx_cache_dir,
        lookback_days=800,
    )
    assert set(market_data.ohlcv_by_symbol.keys()) == {"005930", "086520"}
    assert market_data.data_source == "cache"
    assert len(market_data.ohlcv_by_symbol["005930"]) >= 60


def test_universe_backtest_with_cached_krx_data(krx_cache_dir: Path, tmp_path: Path) -> None:
    service = BacktestService()
    universe = Path("tests/fixtures/universe_krx_mini.csv")
    result = service.run_universe_backtest(
        universe,
        rule_ids=("TR0001", "TR0002"),
        use_cache=True,
        fetch_missing=False,
        cache_dir=krx_cache_dir,
        output_dir=tmp_path / "reports",
    )
    assert result.run_result.data_source.startswith("krx:")
    assert len(result.run_result.rule_results) == 4
    rule_ids = {item.rule_id for item in result.run_result.rule_results}
    assert rule_ids == {"TR0001", "TR0002"}
    assert result.report_path.exists()
    assert all(path.exists() for path in result.markdown_paths)
