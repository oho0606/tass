"""RK0017 — Daily Range Above 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0017DailyRangeAbove20PeriodAverageRule(SpecRule):
    rule_id = "RK0017"
    rule_name = "Daily Range Above 20-Period Average"


def evaluate_rk0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0017."""
    return run_spec_rule(RK0017DailyRangeAbove20PeriodAverageRule, df)
