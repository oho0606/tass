"""MA0002 — Price Above SMA20. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0002PriceAboveSMA20Rule(PricePositionRule):
    rule_id = "MA0002"
    rule_name = "Price Above SMA20"
    ma_type = "sma"
    period = 20
    direction = "above"


def evaluate_ma0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0002."""
    return run_price_position_rule(MA0002PriceAboveSMA20Rule, df)
