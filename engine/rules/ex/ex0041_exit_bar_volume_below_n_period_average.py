"""EX0041 — Exit Bar Volume Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0041ExitBarVolumeBelowNPeriodAverageRule(SpecRule):
    rule_id = "EX0041"
    rule_name = "Exit Bar Volume Below N-Period Average"


def evaluate_ex0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0041."""
    return run_spec_rule(EX0041ExitBarVolumeBelowNPeriodAverageRule, df)
