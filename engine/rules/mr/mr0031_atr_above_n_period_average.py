"""MR0031 — ATR Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0031ATRAboveNPeriodAverageRule(SpecRule):
    rule_id = "MR0031"
    rule_name = "ATR Above N-Period Average"


def evaluate_mr0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0031."""
    return run_spec_rule(MR0031ATRAboveNPeriodAverageRule, df)
