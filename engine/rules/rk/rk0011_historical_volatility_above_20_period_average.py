"""RK0011 — Historical Volatility Above 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0011HistoricalVolatilityAbove20PeriodAverageRule(SpecRule):
    rule_id = "RK0011"
    rule_name = "Historical Volatility Above 20-Period Average"


def evaluate_rk0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0011."""
    return run_spec_rule(RK0011HistoricalVolatilityAbove20PeriodAverageRule, df)
