"""MR0012 — Close Below SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0012CloseBelowSMA60Rule(SpecRule):
    rule_id = "MR0012"
    rule_name = "Close Below SMA60"


def evaluate_mr0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0012."""
    return run_spec_rule(MR0012CloseBelowSMA60Rule, df)
