"""MO0008 — RSI Cross Below 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0008RSICrossBelow50Rule(SpecRule):
    rule_id = "MO0008"
    rule_name = "RSI Cross Below 50"


def evaluate_mo0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0008."""
    return run_spec_rule(MO0008RSICrossBelow50Rule, df)
