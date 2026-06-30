"""RK0012 — Historical Volatility Below 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0012HistoricalVolatilityBelow20PeriodAverageRule(SpecRule):
    rule_id = "RK0012"
    rule_name = "Historical Volatility Below 20-Period Average"


def evaluate_rk0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0012."""
    return run_spec_rule(RK0012HistoricalVolatilityBelow20PeriodAverageRule, df)
