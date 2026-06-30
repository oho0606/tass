"""MR0033 — Historical Volatility Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0033HistoricalVolatilityAboveNPeriodAverageRule(SpecRule):
    rule_id = "MR0033"
    rule_name = "Historical Volatility Above N-Period Average"


def evaluate_mr0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0033."""
    return run_spec_rule(MR0033HistoricalVolatilityAboveNPeriodAverageRule, df)
