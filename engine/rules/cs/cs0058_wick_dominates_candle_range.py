"""CS0058 — Wick Dominates Candle Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0058WickDominatesCandleRangeRule(SpecRule):
    rule_id = "CS0058"
    rule_name = "Wick Dominates Candle Range"


def evaluate_cs0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0058."""
    return run_spec_rule(CS0058WickDominatesCandleRangeRule, df)
