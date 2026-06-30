"""MR0004 — SMA20 Above SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0004SMA20AboveSMA60Rule(SpecRule):
    rule_id = "MR0004"
    rule_name = "SMA20 Above SMA60"


def evaluate_mr0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0004."""
    return run_spec_rule(MR0004SMA20AboveSMA60Rule, df)
