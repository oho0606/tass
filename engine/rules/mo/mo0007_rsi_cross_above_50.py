"""MO0007 — RSI Cross Above 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0007RSICrossAbove50Rule(SpecRule):
    rule_id = "MO0007"
    rule_name = "RSI Cross Above 50"


def evaluate_mo0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0007."""
    return run_spec_rule(MO0007RSICrossAbove50Rule, df)
