"""RK0001 — ATR Above 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0001ATRAbove20PeriodAverageRule(SpecRule):
    rule_id = "RK0001"
    rule_name = "ATR Above 20-Period Average"


def evaluate_rk0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0001."""
    return run_spec_rule(RK0001ATRAbove20PeriodAverageRule, df)
