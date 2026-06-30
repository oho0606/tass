from pathlib import Path

import pandas as pd

from engine.data.universe import load_universe
from engine.domains.moving_average_engine import evaluate_moving_average_engine
from engine.domains.trend_engine import evaluate_trend_engine
from engine.domains.volume_engine import evaluate_volume_engine
from engine.gate.basic_gate import GateConfig, evaluate_basic_gate
from engine.indicators.registry import compute_all
from engine.recommendation.top20 import build_candidate, rank_top20
from engine.scoring import compute_master_score
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def test_e2e_pipeline_synthetic_universe(tmp_path: Path):
    """End-to-end without network: synthetic OHLCV for sample universe."""
    universe_csv = tmp_path / "universe.csv"
    universe_csv.write_text(
        "symbol,name,market\n005930,삼성전자,KS\n000660,SK하이닉스,KS\n",
        encoding="utf-8",
    )
    entries = load_universe(universe_csv)
    gate_cfg = GateConfig(min_traded_value_ma20=0, trend_floor_score=0)

    candidates = []
    for entry in entries:
        df = make_uptrend_ohlcv(n=260, start=100 + int(entry.symbol[:2]))
        df = compute_all(df)
        trend = evaluate_trend_engine(df)
        moving_average = evaluate_moving_average_engine(df)
        volume = evaluate_volume_engine(df)
        master = compute_master_score(
            trend=trend,
            moving_average=moving_average,
            volume=volume,
            mvp_mode=True,
        )
        gate = evaluate_basic_gate(df, trend, data_valid=True, config=gate_cfg)
        candidates.append(
            build_candidate(entry, master, trend, gate.status, df=df, gate=gate, data_valid=True)
        )

    picks = rank_top20(candidates, top_n=2)
    assert len(picks.picks) == 2
    assert picks.picks[0].rank == 1
    assert picks.picks[0].total_score >= picks.picks[1].total_score
    assert picks.picks[0].domains["trend"]["max"] == 200
    assert picks.picks[0].domains["moving_average"]["max"] == 150
    assert picks.picks[0].domains["volume"]["max"] == 150
    assert picks.picks[0].gate == "PASS"
    assert picks.picks[0].probability is not None
    assert picks.picks[0].recommendation is not None
    assert all(pick.gate != "FAIL" for pick in picks.picks)


def test_gate_fails_low_liquidity():
    df = make_uptrend_ohlcv()
    df = compute_all(df)
    df["traded_value_ma_20"] = 1.0
    trend = evaluate_trend_engine(df)
    gate = evaluate_basic_gate(
        df, trend, data_valid=True, config=GateConfig(min_traded_value_ma20=500_000_000)
    )
    assert gate.status == "FAIL"
    assert "Liquidity" in gate.failed_gates
