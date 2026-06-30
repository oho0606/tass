"""PA0011 — Bullish Candle. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0011BullishCandleRule(SpecRule):
    rule_id = "PA0011"
    rule_name = "Bullish Candle"


def evaluate_pa0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0011."""
    return run_spec_rule(PA0011BullishCandleRule, df)
