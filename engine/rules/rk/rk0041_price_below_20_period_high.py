"""RK0041 — Price Below 20-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0041PriceBelow20PeriodHighRule(SpecRule):
    rule_id = "RK0041"
    rule_name = "Price Below 20-Period High"


def evaluate_rk0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0041."""
    return run_spec_rule(RK0041PriceBelow20PeriodHighRule, df)
