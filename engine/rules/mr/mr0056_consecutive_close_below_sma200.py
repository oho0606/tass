"""MR0056 — Consecutive Close Below SMA200. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0056ConsecutiveCloseBelowSMA200Rule(SpecRule):
    rule_id = "MR0056"
    rule_name = "Consecutive Close Below SMA200"


def evaluate_mr0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0056."""
    return run_spec_rule(MR0056ConsecutiveCloseBelowSMA200Rule, df)
