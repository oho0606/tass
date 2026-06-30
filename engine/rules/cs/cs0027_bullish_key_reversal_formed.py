"""CS0027 — Bullish Key Reversal Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0027BullishKeyReversalFormedRule(SpecRule):
    rule_id = "CS0027"
    rule_name = "Bullish Key Reversal Formed"


def evaluate_cs0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0027."""
    return run_spec_rule(CS0027BullishKeyReversalFormedRule, df)
