"""MR0008 — SMA200 Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0008SMA200RisingRule(SpecRule):
    rule_id = "MR0008"
    rule_name = "SMA200 Rising"


def evaluate_mr0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0008."""
    return run_spec_rule(MR0008SMA200RisingRule, df)
