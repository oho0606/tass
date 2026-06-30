"""MR0003 — Close Above SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0003CloseAboveSMA20Rule(SpecRule):
    rule_id = "MR0003"
    rule_name = "Close Above SMA20"


def evaluate_mr0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0003."""
    return run_spec_rule(MR0003CloseAboveSMA20Rule, df)
