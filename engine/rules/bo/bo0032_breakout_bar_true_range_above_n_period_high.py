"""BO0032 — Breakout Bar True Range Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0032BreakoutBarTrueRangeAboveNPeriodHighRule(SpecRule):
    rule_id = "BO0032"
    rule_name = "Breakout Bar True Range Above N-Period High"


def evaluate_bo0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0032."""
    return run_spec_rule(BO0032BreakoutBarTrueRangeAboveNPeriodHighRule, df)
