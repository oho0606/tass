"""MR0024 — Close Within N-Period Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0024CloseWithinNPeriodRangeRule(SpecRule):
    rule_id = "MR0024"
    rule_name = "Close Within N-Period Range"


def evaluate_mr0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0024."""
    return run_spec_rule(MR0024CloseWithinNPeriodRangeRule, df)
