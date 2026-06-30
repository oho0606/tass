"""RK0026 — Unfilled Gap Down Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0026UnfilledGapDownPresentRule(SpecRule):
    rule_id = "RK0026"
    rule_name = "Unfilled Gap Down Present"


def evaluate_rk0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0026."""
    return run_spec_rule(RK0026UnfilledGapDownPresentRule, df)
