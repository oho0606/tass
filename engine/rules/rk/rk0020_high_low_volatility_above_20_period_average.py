"""RK0020 — High-Low Volatility Above 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0020HighLowVolatilityAbove20PeriodAverageRule(SpecRule):
    rule_id = "RK0020"
    rule_name = "High-Low Volatility Above 20-Period Average"


def evaluate_rk0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0020."""
    return run_spec_rule(RK0020HighLowVolatilityAbove20PeriodAverageRule, df)
