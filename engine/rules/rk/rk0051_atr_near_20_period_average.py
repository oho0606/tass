"""RK0051 — ATR Near 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0051ATRNear20PeriodAverageRule(SpecRule):
    rule_id = "RK0051"
    rule_name = "ATR Near 20-Period Average"


def evaluate_rk0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0051."""
    return run_spec_rule(RK0051ATRNear20PeriodAverageRule, df)
