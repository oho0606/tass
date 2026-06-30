"""MA0015 — Price Above EMA240. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0015PriceAboveEMA240Rule(PricePositionRule):
    rule_id = "MA0015"
    rule_name = "Price Above EMA240"
    ma_type = "ema"
    period = 240
    direction = "above"


def evaluate_ma0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0015."""
    return run_price_position_rule(MA0015PriceAboveEMA240Rule, df)
