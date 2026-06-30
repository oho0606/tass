"""MA0016 — Price Below EMA5. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0016PriceBelowEMA5Rule(PricePositionRule):
    rule_id = "MA0016"
    rule_name = "Price Below EMA5"
    ma_type = "ema"
    period = 5
    direction = "below"


def evaluate_ma0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0016."""
    return run_price_position_rule(MA0016PriceBelowEMA5Rule, df)
