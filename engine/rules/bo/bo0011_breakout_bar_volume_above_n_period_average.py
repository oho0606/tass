"""BO0011 — Breakout Bar Volume Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0011BreakoutBarVolumeAboveNPeriodAverageRule(SpecRule):
    rule_id = "BO0011"
    rule_name = "Breakout Bar Volume Above N-Period Average"


def evaluate_bo0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0011."""
    return run_spec_rule(BO0011BreakoutBarVolumeAboveNPeriodAverageRule, df)
