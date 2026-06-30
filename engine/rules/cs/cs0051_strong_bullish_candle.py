"""CS0051 — Strong Bullish Candle. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0051StrongBullishCandleRule(SpecRule):
    rule_id = "CS0051"
    rule_name = "Strong Bullish Candle"


def evaluate_cs0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0051."""
    return run_spec_rule(CS0051StrongBullishCandleRule, df)
