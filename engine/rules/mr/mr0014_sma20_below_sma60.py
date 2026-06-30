"""MR0014 — SMA20 Below SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0014SMA20BelowSMA60Rule(SpecRule):
    rule_id = "MR0014"
    rule_name = "SMA20 Below SMA60"


def evaluate_mr0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0014."""
    return run_spec_rule(MR0014SMA20BelowSMA60Rule, df)
