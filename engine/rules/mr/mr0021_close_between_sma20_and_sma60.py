"""MR0021 — Close Between SMA20 And SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0021CloseBetweenSMA20AndSMA60Rule(SpecRule):
    rule_id = "MR0021"
    rule_name = "Close Between SMA20 And SMA60"


def evaluate_mr0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0021."""
    return run_spec_rule(MR0021CloseBetweenSMA20AndSMA60Rule, df)
