"""RK0004 — ATR Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0004ATRFallingRule(SpecRule):
    rule_id = "RK0004"
    rule_name = "ATR Falling"


def evaluate_rk0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0004."""
    return run_spec_rule(RK0004ATRFallingRule, df)
