"""RK0006 — ATR At 20-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0006ATRAt20PeriodLowRule(SpecRule):
    rule_id = "RK0006"
    rule_name = "ATR At 20-Period Low"


def evaluate_rk0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0006."""
    return run_spec_rule(RK0006ATRAt20PeriodLowRule, df)
