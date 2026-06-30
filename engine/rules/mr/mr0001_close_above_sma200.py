"""MR0001 — Close Above SMA200. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0001CloseAboveSMA200Rule(SpecRule):
    rule_id = "MR0001"
    rule_name = "Close Above SMA200"


def evaluate_mr0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0001."""
    return run_spec_rule(MR0001CloseAboveSMA200Rule, df)
