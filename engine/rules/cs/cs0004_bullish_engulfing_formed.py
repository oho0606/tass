"""CS0004 — Bullish Engulfing Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0004BullishEngulfingFormedRule(SpecRule):
    rule_id = "CS0004"
    rule_name = "Bullish Engulfing Formed"


def evaluate_cs0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0004."""
    return run_spec_rule(CS0004BullishEngulfingFormedRule, df)
