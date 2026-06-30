"""CS0023 — Bullish Abandoned Baby Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0023BullishAbandonedBabyFormedRule(SpecRule):
    rule_id = "CS0023"
    rule_name = "Bullish Abandoned Baby Formed"


def evaluate_cs0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0023."""
    return run_spec_rule(CS0023BullishAbandonedBabyFormedRule, df)
