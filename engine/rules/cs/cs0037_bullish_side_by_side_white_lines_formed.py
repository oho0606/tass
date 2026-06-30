"""CS0037 — Bullish Side By Side White Lines Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0037BullishSideBySideWhiteLinesFormedRule(SpecRule):
    rule_id = "CS0037"
    rule_name = "Bullish Side By Side White Lines Formed"


def evaluate_cs0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0037."""
    return run_spec_rule(CS0037BullishSideBySideWhiteLinesFormedRule, df)
