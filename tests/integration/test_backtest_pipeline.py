"""Integration tests for Backtest Engine pipeline."""

from __future__ import annotations

from engine.backtest import BacktestEngine, BacktestRunInput
from tests.fixtures.ohlcv import make_downtrend_ohlcv, make_uptrend_ohlcv


def test_backtest_pipeline_synthetic():
    """End-to-end backtest without network."""
    engine = BacktestEngine()
    result = engine.run(
        BacktestRunInput(
            ohlcv_by_symbol={
                "UP": make_uptrend_ohlcv(n=200),
                "DOWN": make_downtrend_ohlcv(n=200),
            },
            data_source="synthetic",
        )
    )
    assert len(result.rule_results) >= 4
    rule_ids = {item.rule_id for item in result.rule_results}
    assert "TR0001" in rule_ids
    assert all(item.verdict for item in result.rule_results)
