"""MA0011 — Price Above EMA5. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0011PriceAboveEMA5Rule(PricePositionRule):
    rule_id = "MA0011"
    rule_name = "Price Above EMA5"
    ma_type = "ema"
    period = 5
    direction = "above"


def evaluate_ma0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0011."""
    return run_price_position_rule(MA0011PriceAboveEMA5Rule, df)
