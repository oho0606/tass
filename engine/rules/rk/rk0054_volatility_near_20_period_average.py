"""RK0054 — Volatility Near 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0054VolatilityNear20PeriodAverageRule(SpecRule):
    rule_id = "RK0054"
    rule_name = "Volatility Near 20-Period Average"


def evaluate_rk0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0054."""
    return run_spec_rule(RK0054VolatilityNear20PeriodAverageRule, df)
