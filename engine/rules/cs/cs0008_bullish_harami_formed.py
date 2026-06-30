"""CS0008 — Bullish Harami Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0008BullishHaramiFormedRule(SpecRule):
    rule_id = "CS0008"
    rule_name = "Bullish Harami Formed"


def evaluate_cs0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0008."""
    return run_spec_rule(CS0008BullishHaramiFormedRule, df)
