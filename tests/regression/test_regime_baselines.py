"""Multi-regime regression baselines (Phase 6)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.backtest import backtest_rule
from engine.backtest.config import load_backtest_config
from engine.rules.tr.tr0001_higher_high import evaluate_higher_high
from tests.fixtures.ohlcv import (
    make_downtrend_ohlcv,
    make_gap_up_ohlcv,
    make_high_volume_ohlcv,
    make_sideways_ohlcv,
    make_uptrend_ohlcv,
)

BASELINE_DIR = Path("tests/regression/baselines/regimes")
TOLERANCE = {"win_rate": 0.05, "profit_factor": 0.2, "trade_count": 2}

REGIMES = {
    "bull": ("SYN_UP", make_uptrend_ohlcv),
    "bear": ("SYN_DOWN", make_downtrend_ohlcv),
    "sideways": ("SYN_SIDE", make_sideways_ohlcv),
    "gap_up": ("SYN_GAP", make_gap_up_ohlcv),
    "high_volume": ("SYN_VOL", make_high_volume_ohlcv),
}


def _baseline_path(name: str) -> Path:
    return BASELINE_DIR / f"tr0001_{name}.json"


def _load_or_create(name: str, metrics: dict) -> dict | None:
    path = _baseline_path(name)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
        return None
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.mark.regression
@pytest.mark.parametrize("regime_name", list(REGIMES.keys()))
def test_tr0001_regime_baseline(regime_name: str):
    """TR0001 metrics must stay stable across market regime fixtures."""
    symbol, factory = REGIMES[regime_name]
    cfg = load_backtest_config()
    df = factory(n=200)
    result = backtest_rule("TR0001", symbol, df, evaluate_higher_high, cfg)
    current = {
        "win_rate": result.metrics.win_rate,
        "profit_factor": result.metrics.profit_factor,
        "trade_count": result.metrics.trade_count,
        "verdict": result.verdict,
    }

    baseline = _load_or_create(regime_name, current)
    if baseline is None:
        pytest.skip(f"Baseline created for regime={regime_name}; re-run to validate.")

    for key, tolerance in TOLERANCE.items():
        if key not in baseline:
            continue
        assert abs(float(current[key]) - float(baseline[key])) <= tolerance, (
            f"{regime_name}.{key}: {current[key]} vs {baseline[key]}"
        )
