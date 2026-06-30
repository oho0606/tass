"""CS0052 — Strong Bearish Candle. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0052StrongBearishCandleRule(SpecRule):
    rule_id = "CS0052"
    rule_name = "Strong Bearish Candle"


def evaluate_cs0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0052."""
    return run_spec_rule(CS0052StrongBearishCandleRule, df)
