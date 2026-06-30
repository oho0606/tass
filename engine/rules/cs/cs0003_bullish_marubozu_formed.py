"""CS0003 — Bullish Marubozu Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0003BullishMarubozuFormedRule(SpecRule):
    rule_id = "CS0003"
    rule_name = "Bullish Marubozu Formed"


def evaluate_cs0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0003."""
    return run_spec_rule(CS0003BullishMarubozuFormedRule, df)
