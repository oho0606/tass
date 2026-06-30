"""BO0033 — Breakout Bar ATR Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0033BreakoutBarATRAboveNPeriodAverageRule(SpecRule):
    rule_id = "BO0033"
    rule_name = "Breakout Bar ATR Above N-Period Average"


def evaluate_bo0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0033."""
    return run_spec_rule(BO0033BreakoutBarATRAboveNPeriodAverageRule, df)
