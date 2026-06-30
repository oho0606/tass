"""Tests for market context and pipeline gate reports."""

from __future__ import annotations

from engine.domains.moving_average_engine import evaluate_moving_average_engine
from engine.domains.trend_engine import evaluate_trend_engine
from engine.domains.volume_engine import evaluate_volume_engine
from engine.gate.config import GateConfig, merge_gate_config
from engine.gate.evaluate import evaluate_symbol_gates
from engine.gate.market_context import (
    classify_index_trend,
    resolve_effective_market_trend,
    worst_market_trend,
)
from engine.gate.models import GateResult, GateStatus, PipelineResult
from engine.gate.report import build_pipeline_gate_report
from engine.indicators.registry import compute_all
from engine.scoring import compute_master_score
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def test_worst_market_trend_prefers_crash():
    assert worst_market_trend("UP", "DOWN", "CRASH") == "CRASH"
    assert worst_market_trend("UP", "DOWN") == "DOWN"


def test_resolve_effective_market_trend_listing_mode():
    assert (
        resolve_effective_market_trend(
            kospi_trend="UP",
            kosdaq_trend="CRASH",
            listing_market="KS",
            combine_mode="listing",
        )
        == "UP"
    )
    assert (
        resolve_effective_market_trend(
            kospi_trend="UP",
            kosdaq_trend="CRASH",
            listing_market="KQ",
            combine_mode="listing",
        )
        == "CRASH"
    )
    assert (
        resolve_effective_market_trend(
            kospi_trend="UP",
            kosdaq_trend="CRASH",
            combine_mode="worst",
        )
        == "CRASH"
    )


def test_classify_index_trend_uptrend():
    df = make_uptrend_ohlcv(n=120, start=100)
    assert classify_index_trend(df) == "UP"


def test_classify_index_trend_crash():
    df = make_uptrend_ohlcv(n=120, start=200)
    df.loc[df.index[-10:], "close"] = df["close"].iloc[-10:].values * 0.8
    df.loc[df.index[-10:], "high"] = df["close"]
    df.loc[df.index[-10:], "low"] = df["close"]
    assert classify_index_trend(df, crash_drawdown=0.05) == "CRASH"


def test_pipeline_gate_report_contains_pipeline_source():
    df = compute_all(make_uptrend_ohlcv(n=260))
    trend = evaluate_trend_engine(df)
    master = compute_master_score(
        trend=trend,
        moving_average=evaluate_moving_average_engine(df),
        volume=evaluate_volume_engine(df),
        mvp_mode=True,
    )
    evaluation = evaluate_symbol_gates(
        df=df,
        trend=trend,
        data_valid=True,
        gate_cfg=GateConfig(min_traded_value_ma20=0, trend_floor_score=0),
        master=master,
        market_context={"kospi_trend": "UP", "kosdaq_trend": "UP", "market_trend": "UP"},
    )

    assert evaluation.gate_report
    assert all(item["source"] == "pipeline" for item in evaluation.gate_report)
    assert evaluation.gate_report[0]["gate_key"] == "data_quality"


def test_build_pipeline_gate_report_warning_includes_deduction():
    result = PipelineResult(
        is_passed=True,
        final_score=880,
        total_deduction=20,
        gate_results=[
            GateResult("MarketGate", GateStatus.WARNING, "Market down", deduction=20),
        ],
    )
    config = merge_gate_config({}, GateConfig())
    reports = build_pipeline_gate_report(
        result,
        data={"kospi_trend": "DOWN", "kosdaq_trend": "UP", "market_trend": "DOWN"},
        config=config,
    )

    assert reports[0]["status"] == "WARNING"
    assert reports[0]["deduction"] == 20
