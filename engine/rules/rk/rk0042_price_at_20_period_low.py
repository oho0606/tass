"""RK0042 — Price At 20-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0042PriceAt20PeriodLowRule(SpecRule):
    rule_id = "RK0042"
    rule_name = "Price At 20-Period Low"


def evaluate_rk0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0042."""
    return run_spec_rule(RK0042PriceAt20PeriodLowRule, df)
