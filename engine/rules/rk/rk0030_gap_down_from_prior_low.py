"""RK0030 — Gap Down From Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0030GapDownFromPriorLowRule(SpecRule):
    rule_id = "RK0030"
    rule_name = "Gap Down From Prior Low"


def evaluate_rk0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0030."""
    return run_spec_rule(RK0030GapDownFromPriorLowRule, df)
