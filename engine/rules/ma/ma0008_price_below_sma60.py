"""MA0008 — Price Below SMA60. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0008PriceBelowSMA60Rule(PricePositionRule):
    rule_id = "MA0008"
    rule_name = "Price Below SMA60"
    ma_type = "sma"
    period = 60
    direction = "below"


def evaluate_ma0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0008."""
    return run_price_position_rule(MA0008PriceBelowSMA60Rule, df)
