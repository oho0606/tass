"""CS0039 — Bullish Separating Lines Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0039BullishSeparatingLinesFormedRule(SpecRule):
    rule_id = "CS0039"
    rule_name = "Bullish Separating Lines Formed"


def evaluate_cs0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0039."""
    return run_spec_rule(CS0039BullishSeparatingLinesFormedRule, df)
