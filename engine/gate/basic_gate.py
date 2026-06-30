from __future__ import annotations

import pandas as pd

from engine.core.types import GateResult, TrendEngineResult
from engine.gate.config import GateConfig
from engine.gate.evaluate import evaluate_symbol_gates
from engine.scoring import compute_master_score

__all__ = ["GateConfig", "compute_master_score", "evaluate_basic_gate"]


def evaluate_basic_gate(
    df: pd.DataFrame,
    trend: TrendEngineResult,
    data_valid: bool,
    config: GateConfig | None = None,
) -> GateResult:
    """Evaluate TASS-006 gate pipeline and return legacy ``GateResult``."""
    evaluation = evaluate_symbol_gates(
        df=df,
        trend=trend,
        data_valid=data_valid,
        gate_cfg=config,
    )
    return evaluation.legacy_gate
