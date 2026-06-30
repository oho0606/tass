"""RK0035 — Turnover Below 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0035TurnoverBelow20PeriodAverageRule(SpecRule):
    rule_id = "RK0035"
    rule_name = "Turnover Below 20-Period Average"


def evaluate_rk0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0035."""
    return run_spec_rule(RK0035TurnoverBelow20PeriodAverageRule, df)
