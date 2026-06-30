"""CS0010 — Bullish Kicker Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0010BullishKickerFormedRule(SpecRule):
    rule_id = "CS0010"
    rule_name = "Bullish Kicker Formed"


def evaluate_cs0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0010."""
    return run_spec_rule(CS0010BullishKickerFormedRule, df)
