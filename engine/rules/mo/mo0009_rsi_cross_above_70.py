"""MO0009 — RSI Cross Above 70. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0009RSICrossAbove70Rule(SpecRule):
    rule_id = "MO0009"
    rule_name = "RSI Cross Above 70"


def evaluate_mo0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0009."""
    return run_spec_rule(MO0009RSICrossAbove70Rule, df)
