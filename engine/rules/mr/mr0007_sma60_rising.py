"""MR0007 — SMA60 Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0007SMA60RisingRule(SpecRule):
    rule_id = "MR0007"
    rule_name = "SMA60 Rising"


def evaluate_mr0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0007."""
    return run_spec_rule(MR0007SMA60RisingRule, df)
