"""RK0043 — Current Drawdown Above 10 Percent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0043CurrentDrawdownAbove10PercentRule(SpecRule):
    rule_id = "RK0043"
    rule_name = "Current Drawdown Above 10 Percent"


def evaluate_rk0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0043."""
    return run_spec_rule(RK0043CurrentDrawdownAbove10PercentRule, df)
