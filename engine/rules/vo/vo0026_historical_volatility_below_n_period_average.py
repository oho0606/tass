"""VO0026 — Historical Volatility Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0026HistoricalVolatilityBelowNPeriodAverageRule(SpecRule):
    rule_id = "VO0026"
    rule_name = "Historical Volatility Below N-Period Average"


def evaluate_vo0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0026."""
    return run_spec_rule(VO0026HistoricalVolatilityBelowNPeriodAverageRule, df)
