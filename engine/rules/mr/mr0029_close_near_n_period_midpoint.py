"""MR0029 — Close Near N-Period Midpoint. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0029CloseNearNPeriodMidpointRule(SpecRule):
    rule_id = "MR0029"
    rule_name = "Close Near N-Period Midpoint"


def evaluate_mr0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0029."""
    return run_spec_rule(MR0029CloseNearNPeriodMidpointRule, df)
