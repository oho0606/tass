"""BO0031 — Breakout Bar True Range Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0031BreakoutBarTrueRangeAboveNPeriodAverageRule(SpecRule):
    rule_id = "BO0031"
    rule_name = "Breakout Bar True Range Above N-Period Average"


def evaluate_bo0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0031."""
    return run_spec_rule(BO0031BreakoutBarTrueRangeAboveNPeriodAverageRule, df)
