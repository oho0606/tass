"""MR0015 — SMA60 Below SMA200. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0015SMA60BelowSMA200Rule(SpecRule):
    rule_id = "MR0015"
    rule_name = "SMA60 Below SMA200"


def evaluate_mr0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0015."""
    return run_spec_rule(MR0015SMA60BelowSMA200Rule, df)
