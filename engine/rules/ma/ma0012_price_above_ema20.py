"""MA0012 — Price Above EMA20. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0012PriceAboveEMA20Rule(PricePositionRule):
    rule_id = "MA0012"
    rule_name = "Price Above EMA20"
    ma_type = "ema"
    period = 20
    direction = "above"


def evaluate_ma0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0012."""
    return run_price_position_rule(MA0012PriceAboveEMA20Rule, df)
