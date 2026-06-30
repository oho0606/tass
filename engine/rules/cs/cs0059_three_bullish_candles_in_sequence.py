"""CS0059 — Three Bullish Candles In Sequence. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0059ThreeBullishCandlesInSequenceRule(SpecRule):
    rule_id = "CS0059"
    rule_name = "Three Bullish Candles In Sequence"


def evaluate_cs0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0059."""
    return run_spec_rule(CS0059ThreeBullishCandlesInSequenceRule, df)
