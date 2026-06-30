"""RK0059 — Gap Frequency Above 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0059GapFrequencyAbove20PeriodAverageRule(SpecRule):
    rule_id = "RK0059"
    rule_name = "Gap Frequency Above 20-Period Average"


def evaluate_rk0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0059."""
    return run_spec_rule(RK0059GapFrequencyAbove20PeriodAverageRule, df)
