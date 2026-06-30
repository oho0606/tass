"""CS0033 — Bullish Mat Hold Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0033BullishMatHoldFormedRule(SpecRule):
    rule_id = "CS0033"
    rule_name = "Bullish Mat Hold Formed"


def evaluate_cs0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0033."""
    return run_spec_rule(CS0033BullishMatHoldFormedRule, df)
