"""CS0009 — Bullish Belt Hold Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0009BullishBeltHoldFormedRule(SpecRule):
    rule_id = "CS0009"
    rule_name = "Bullish Belt Hold Formed"


def evaluate_cs0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0009."""
    return run_spec_rule(CS0009BullishBeltHoldFormedRule, df)
