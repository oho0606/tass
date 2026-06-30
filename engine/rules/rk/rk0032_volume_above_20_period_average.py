"""RK0032 — Volume Above 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0032VolumeAbove20PeriodAverageRule(SpecRule):
    rule_id = "RK0032"
    rule_name = "Volume Above 20-Period Average"


def evaluate_rk0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0032."""
    return run_spec_rule(RK0032VolumeAbove20PeriodAverageRule, df)
