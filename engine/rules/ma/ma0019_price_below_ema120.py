"""MA0019 — Price Below EMA120. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0019PriceBelowEMA120Rule(PricePositionRule):
    rule_id = "MA0019"
    rule_name = "Price Below EMA120"
    ma_type = "ema"
    period = 120
    direction = "below"


def evaluate_ma0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0019."""
    return run_price_position_rule(MA0019PriceBelowEMA120Rule, df)
