"""Regression tests for TR Rule backtest metrics (TASS-030 §15)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.backtest import BacktestEngine, BacktestRunInput, backtest_rule
from engine.backtest.config import load_backtest_config
from engine.rules.tr.tr0001_higher_high import evaluate_higher_high
from tests.fixtures.ohlcv import make_uptrend_ohlcv

BASELINE_PATH = Path("tests/regression/baselines/tr0001_synthetic.json")
TOLERANCE = {
    "win_rate": 0.05,
    "profit_factor": 0.2,
    "trade_count": 2,
}


def _load_baseline() -> dict[str, float | int]:
    if not BASELINE_PATH.exists():
        return {}
    with BASELINE_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def _write_baseline(metrics: dict[str, float | int]) -> None:
    BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with BASELINE_PATH.open("w", encoding="utf-8") as handle:
        json.dump(metrics, handle, indent=2)


@pytest.mark.regression
def test_tr0001_backtest_regression():
    """TR0001 synthetic backtest metrics must match stored baseline."""
    cfg = load_backtest_config()
    df = make_uptrend_ohlcv(n=200)
    result = backtest_rule("TR0001", "SYN_UP", df, evaluate_higher_high, cfg)
    current = {
        "win_rate": result.metrics.win_rate,
        "profit_factor": result.metrics.profit_factor,
        "trade_count": result.metrics.trade_count,
        "verdict": result.verdict,
    }

    baseline = _load_baseline()
    if not baseline:
        _write_baseline(current)
        pytest.skip("Baseline created on first run — re-run to validate regression.")

    for key, tolerance in TOLERANCE.items():
        if key not in baseline:
            continue
        assert (
            abs(float(current[key]) - float(baseline[key])) <= tolerance
        ), f"{key}: {current[key]} vs baseline {baseline[key]}"


@pytest.mark.regression
def test_backtest_engine_reproducibility():
    """Identical inputs must produce identical metrics (TASS-009 §16)."""
    run_input = BacktestRunInput(
        ohlcv_by_symbol={"UP": make_uptrend_ohlcv(n=200)},
        rule_ids=("TR0001",),
        data_source="synthetic",
    )
    first = BacktestEngine().run(run_input)
    second = BacktestEngine().run(run_input)
    m1 = first.rule_results[0].metrics
    m2 = second.rule_results[0].metrics
    assert m1.trade_count == m2.trade_count
    assert m1.win_rate == m2.win_rate
    assert m1.profit_factor == m2.profit_factor
