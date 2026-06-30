"""MR0006 — SMA20 Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0006SMA20RisingRule(SpecRule):
    rule_id = "MR0006"
    rule_name = "SMA20 Rising"


def evaluate_mr0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0006."""
    return run_spec_rule(MR0006SMA20RisingRule, df)
