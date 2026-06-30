"""RK0049 — Price Underwater From Peak. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0049PriceUnderwaterFromPeakRule(SpecRule):
    rule_id = "RK0049"
    rule_name = "Price Underwater From Peak"


def evaluate_rk0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0049."""
    return run_spec_rule(RK0049PriceUnderwaterFromPeakRule, df)
