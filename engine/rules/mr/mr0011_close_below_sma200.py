"""MR0011 — Close Below SMA200. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0011CloseBelowSMA200Rule(SpecRule):
    rule_id = "MR0011"
    rule_name = "Close Below SMA200"


def evaluate_mr0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0011."""
    return run_spec_rule(MR0011CloseBelowSMA200Rule, df)
