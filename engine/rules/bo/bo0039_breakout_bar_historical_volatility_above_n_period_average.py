"""BO0039 — Breakout Bar Historical Volatility Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0039BreakoutBarHistoricalVolatilityAboveNPeriodAverageRule(SpecRule):
    rule_id = "BO0039"
    rule_name = "Breakout Bar Historical Volatility Above N-Period Average"


def evaluate_bo0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0039."""
    return run_spec_rule(BO0039BreakoutBarHistoricalVolatilityAboveNPeriodAverageRule, df)
