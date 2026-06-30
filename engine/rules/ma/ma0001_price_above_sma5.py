"""MA0001 — Price Above SMA5. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0001PriceAboveSMA5Rule(PricePositionRule):
    rule_id = "MA0001"
    rule_name = "Price Above SMA5"
    ma_type = "sma"
    period = 5
    direction = "above"


def evaluate_ma0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0001."""
    return run_price_position_rule(MA0001PriceAboveSMA5Rule, df)
