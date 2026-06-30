"""Integration tests for TASS-006 Gate Pipeline."""

from __future__ import annotations

import unittest

import pandas as pd

from engine.domains.trend_engine import evaluate_trend_engine
from engine.gate.config import GateConfig, merge_gate_config
from engine.gate.data_quality_gate import evaluate_data_quality_gate
from engine.gate.factory import build_gate_pipeline
from engine.gate.liquidity_gate import evaluate_liquidity_gate
from engine.gate.market_gate import evaluate_market_gate
from engine.gate.pipeline import GatePipeline
from engine.gate.volatility_gate import evaluate_volatility_gate
from engine.indicators.registry import compute_all
from tests.fixtures.ohlcv import make_uptrend_ohlcv


class TestGatePipelineIntegration(unittest.TestCase):
    def setUp(self):
        self.config = merge_gate_config(
            {
                "market": {"enabled": True, "warning_penalty": 20},
                "volatility": {
                    "enabled": True,
                    "warn_threshold": 0.10,
                    "fail_threshold": 0.15,
                    "warning_penalty": 15,
                },
                "data_quality": {"enabled": False},
                "liquidity": {"enabled": False},
                "trend": {"enabled": False},
            },
            GateConfig(),
        )

        self.pipeline = GatePipeline()
        self.pipeline.add_gate(evaluate_market_gate)
        self.pipeline.add_gate(evaluate_volatility_gate)

    def test_pipeline_warning_deduction(self):
        data = {"kospi_trend": "DOWN", "atr_percent": 0.05}

        result = self.pipeline.evaluate_gate_pipeline(data, self.config, initial_score=900)

        self.assertTrue(result.is_passed)
        self.assertEqual(result.total_deduction, 20)
        self.assertEqual(result.final_score, 880)

    def test_pipeline_short_circuit_fail(self):
        data = {"kospi_trend": "UP", "atr_percent": 0.20}

        result = self.pipeline.evaluate_gate_pipeline(data, self.config, initial_score=900)

        self.assertFalse(result.is_passed)
        self.assertEqual(result.final_score, 0)
        self.assertEqual(result.gate_results[-1].name, "VolatilityGate")
        self.assertEqual(result.gate_results[-1].status.value, "FAIL")

    def test_data_quality_short_circuits_before_market(self):
        pipeline = build_gate_pipeline(
            merge_gate_config(
                {
                    "data_quality": {"enabled": True},
                    "market": {"enabled": True},
                    "liquidity": {"enabled": False},
                    "trend": {"enabled": False},
                    "volatility": {"enabled": False},
                },
                GateConfig(min_bars=60),
            )
        )
        data = {"data_valid": False, "bar_count": 100, "kospi_trend": "CRASH"}

        result = pipeline.evaluate_gate_pipeline(data, self.config, initial_score=900)

        self.assertFalse(result.is_passed)
        self.assertEqual(len(result.gate_results), 1)
        self.assertEqual(result.gate_results[0].name, "DataQualityGate")

    def test_liquidity_gate_fail(self):
        config = merge_gate_config(
            {
                "data_quality": {"enabled": False},
                "market": {"enabled": False},
                "liquidity": {"enabled": True},
                "trend": {"enabled": False},
                "volatility": {"enabled": False},
            },
            GateConfig(min_traded_value_ma20=500_000_000),
        )
        result = evaluate_liquidity_gate(
            {"traded_value_ma20": 1.0},
            config,
        )
        self.assertEqual(result.status.value, "FAIL")

    def test_full_pipeline_with_synthetic_ohlcv(self):
        df = compute_all(make_uptrend_ohlcv(n=260))
        trend = evaluate_trend_engine(df)
        pipeline = build_gate_pipeline(
            merge_gate_config({}, GateConfig(min_traded_value_ma20=0, trend_floor_score=0))
        )
        data = {
            "data_valid": True,
            "bar_count": len(df),
            "traded_value_ma20": df["traded_value_ma_20"].iloc[-1],
            "trend_score": trend.trend_score,
            "kospi_trend": "UP",
            "atr_percent": float(df["atr_14"].iloc[-1] / df["close"].iloc[-1]),
        }
        config = merge_gate_config({}, GateConfig(min_traded_value_ma20=0, trend_floor_score=0))

        result = pipeline.evaluate_gate_pipeline(data, config, initial_score=800)

        self.assertTrue(result.is_passed)
        self.assertGreater(result.final_score, 0)


if __name__ == "__main__":
    unittest.main()
