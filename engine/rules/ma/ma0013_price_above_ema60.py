"""MA0013 — Price Above EMA60. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0013PriceAboveEMA60Rule(PricePositionRule):
    rule_id = "MA0013"
    rule_name = "Price Above EMA60"
    ma_type = "ema"
    period = 60
    direction = "above"


def evaluate_ma0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0013."""
    return run_price_position_rule(MA0013PriceAboveEMA60Rule, df)
