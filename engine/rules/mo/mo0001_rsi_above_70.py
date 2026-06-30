"""MO0001 — RSI Above 70. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0001RSIAbove70Rule(SpecRule):
    rule_id = "MO0001"
    rule_name = "RSI Above 70"


def evaluate_mo0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0001."""
    return run_spec_rule(MO0001RSIAbove70Rule, df)
