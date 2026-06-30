"""MA0010 — Price Below SMA240. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0010PriceBelowSMA240Rule(PricePositionRule):
    rule_id = "MA0010"
    rule_name = "Price Below SMA240"
    ma_type = "sma"
    period = 240
    direction = "below"


def evaluate_ma0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0010."""
    return run_price_position_rule(MA0010PriceBelowSMA240Rule, df)
