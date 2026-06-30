"""MA0018 — Price Below EMA60. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0018PriceBelowEMA60Rule(PricePositionRule):
    rule_id = "MA0018"
    rule_name = "Price Below EMA60"
    ma_type = "ema"
    period = 60
    direction = "below"


def evaluate_ma0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0018."""
    return run_price_position_rule(MA0018PriceBelowEMA60Rule, df)
