"""RK0050 — Price Above Prior Peak. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0050PriceAbovePriorPeakRule(SpecRule):
    rule_id = "RK0050"
    rule_name = "Price Above Prior Peak"


def evaluate_rk0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0050."""
    return run_spec_rule(RK0050PriceAbovePriorPeakRule, df)
