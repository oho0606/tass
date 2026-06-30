"""MA0009 — Price Below SMA120. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0009PriceBelowSMA120Rule(PricePositionRule):
    rule_id = "MA0009"
    rule_name = "Price Below SMA120"
    ma_type = "sma"
    period = 120
    direction = "below"


def evaluate_ma0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0009."""
    return run_price_position_rule(MA0009PriceBelowSMA120Rule, df)
