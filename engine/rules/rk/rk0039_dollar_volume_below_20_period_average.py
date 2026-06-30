"""RK0039 — Dollar Volume Below 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0039DollarVolumeBelow20PeriodAverageRule(SpecRule):
    rule_id = "RK0039"
    rule_name = "Dollar Volume Below 20-Period Average"


def evaluate_rk0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0039."""
    return run_spec_rule(RK0039DollarVolumeBelow20PeriodAverageRule, df)
