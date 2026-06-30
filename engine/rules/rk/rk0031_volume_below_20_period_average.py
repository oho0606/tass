"""RK0031 — Volume Below 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0031VolumeBelow20PeriodAverageRule(SpecRule):
    rule_id = "RK0031"
    rule_name = "Volume Below 20-Period Average"


def evaluate_rk0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0031."""
    return run_spec_rule(RK0031VolumeBelow20PeriodAverageRule, df)
