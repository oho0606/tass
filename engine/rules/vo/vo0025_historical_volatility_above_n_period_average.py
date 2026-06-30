"""VO0025 — Historical Volatility Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0025HistoricalVolatilityAboveNPeriodAverageRule(SpecRule):
    rule_id = "VO0025"
    rule_name = "Historical Volatility Above N-Period Average"


def evaluate_vo0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0025."""
    return run_spec_rule(VO0025HistoricalVolatilityAboveNPeriodAverageRule, df)
