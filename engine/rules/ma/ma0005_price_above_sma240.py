"""MA0005 — Price Above SMA240. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0005PriceAboveSMA240Rule(PricePositionRule):
    rule_id = "MA0005"
    rule_name = "Price Above SMA240"
    ma_type = "sma"
    period = 240
    direction = "above"


def evaluate_ma0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0005."""
    return run_price_position_rule(MA0005PriceAboveSMA240Rule, df)
