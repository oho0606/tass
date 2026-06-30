"""MR0041 — ATR Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0041ATRBelowNPeriodAverageRule(SpecRule):
    rule_id = "MR0041"
    rule_name = "ATR Below N-Period Average"


def evaluate_mr0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0041."""
    return run_spec_rule(MR0041ATRBelowNPeriodAverageRule, df)
