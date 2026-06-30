"""MR0043 — Historical Volatility Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0043HistoricalVolatilityBelowNPeriodAverageRule(SpecRule):
    rule_id = "MR0043"
    rule_name = "Historical Volatility Below N-Period Average"


def evaluate_mr0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0043."""
    return run_spec_rule(MR0043HistoricalVolatilityBelowNPeriodAverageRule, df)
