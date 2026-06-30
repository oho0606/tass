"""BO0012 — Breakout Bar Volume Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0012BreakoutBarVolumeBelowNPeriodAverageRule(SpecRule):
    rule_id = "BO0012"
    rule_name = "Breakout Bar Volume Below N-Period Average"


def evaluate_bo0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0012."""
    return run_spec_rule(BO0012BreakoutBarVolumeBelowNPeriodAverageRule, df)
