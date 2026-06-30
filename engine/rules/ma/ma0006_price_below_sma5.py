"""MA0006 — Price Below SMA5. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0006PriceBelowSMA5Rule(PricePositionRule):
    rule_id = "MA0006"
    rule_name = "Price Below SMA5"
    ma_type = "sma"
    period = 5
    direction = "below"


def evaluate_ma0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0006."""
    return run_price_position_rule(MA0006PriceBelowSMA5Rule, df)
