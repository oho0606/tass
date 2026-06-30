"""RK0044 — Current Drawdown Below 10 Percent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0044CurrentDrawdownBelow10PercentRule(SpecRule):
    rule_id = "RK0044"
    rule_name = "Current Drawdown Below 10 Percent"


def evaluate_rk0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0044."""
    return run_spec_rule(RK0044CurrentDrawdownBelow10PercentRule, df)
