from __future__ import annotations

from typing import Any, Callable, Dict

from engine.gate.data_quality_gate import evaluate_data_quality_gate
from engine.gate.liquidity_gate import evaluate_liquidity_gate
from engine.gate.market_gate import evaluate_market_gate
from engine.gate.models import GateResult
from engine.gate.pipeline import GatePipeline
from engine.gate.trend_gate import evaluate_trend_gate
from engine.gate.volatility_gate import evaluate_volatility_gate

# TASS-006 우선순위: Data Quality → Market → Liquidity → Trend → Volatility
GATE_REGISTRY: list[tuple[str, Callable[[Dict[str, Any], Dict[str, Any]], GateResult]]] = [
    ("data_quality", evaluate_data_quality_gate),
    ("market", evaluate_market_gate),
    ("liquidity", evaluate_liquidity_gate),
    ("trend", evaluate_trend_gate),
    ("volatility", evaluate_volatility_gate),
]


def build_gate_pipeline(config: Dict[str, Dict[str, Any]]) -> GatePipeline:
    """Build a pipeline with enabled gates in TASS-006 order."""
    pipeline = GatePipeline()
    for key, gate_func in GATE_REGISTRY:
        section = config.get(key, {})
        if section.get("enabled", True):
            pipeline.add_gate(gate_func)
    return pipeline
