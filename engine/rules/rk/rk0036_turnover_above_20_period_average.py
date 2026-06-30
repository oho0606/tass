"""RK0036 — Turnover Above 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0036TurnoverAbove20PeriodAverageRule(SpecRule):
    rule_id = "RK0036"
    rule_name = "Turnover Above 20-Period Average"


def evaluate_rk0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0036."""
    return run_spec_rule(RK0036TurnoverAbove20PeriodAverageRule, df)
