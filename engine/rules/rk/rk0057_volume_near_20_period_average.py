"""RK0057 — Volume Near 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0057VolumeNear20PeriodAverageRule(SpecRule):
    rule_id = "RK0057"
    rule_name = "Volume Near 20-Period Average"


def evaluate_rk0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0057."""
    return run_spec_rule(RK0057VolumeNear20PeriodAverageRule, df)
