"""MA0007 — Price Below SMA20. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0007PriceBelowSMA20Rule(PricePositionRule):
    rule_id = "MA0007"
    rule_name = "Price Below SMA20"
    ma_type = "sma"
    period = 20
    direction = "below"


def evaluate_ma0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0007."""
    return run_price_position_rule(MA0007PriceBelowSMA20Rule, df)
