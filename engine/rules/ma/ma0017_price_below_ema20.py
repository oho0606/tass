"""MA0017 — Price Below EMA20. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0017PriceBelowEMA20Rule(PricePositionRule):
    rule_id = "MA0017"
    rule_name = "Price Below EMA20"
    ma_type = "ema"
    period = 20
    direction = "below"


def evaluate_ma0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0017."""
    return run_price_position_rule(MA0017PriceBelowEMA20Rule, df)
