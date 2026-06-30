"""RK0002 — ATR Below 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0002ATRBelow20PeriodAverageRule(SpecRule):
    rule_id = "RK0002"
    rule_name = "ATR Below 20-Period Average"


def evaluate_rk0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0002."""
    return run_spec_rule(RK0002ATRBelow20PeriodAverageRule, df)
