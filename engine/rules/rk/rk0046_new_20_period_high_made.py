"""RK0046 — New 20-Period High Made. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0046New20PeriodHighMadeRule(SpecRule):
    rule_id = "RK0046"
    rule_name = "New 20-Period High Made"


def evaluate_rk0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0046."""
    return run_spec_rule(RK0046New20PeriodHighMadeRule, df)
