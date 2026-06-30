"""MR0037 — True Range Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0037TrueRangeAboveNPeriodAverageRule(SpecRule):
    rule_id = "MR0037"
    rule_name = "True Range Above N-Period Average"


def evaluate_mr0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0037."""
    return run_spec_rule(MR0037TrueRangeAboveNPeriodAverageRule, df)
