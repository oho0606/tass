"""MA0004 — Price Above SMA120. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0004PriceAboveSMA120Rule(PricePositionRule):
    rule_id = "MA0004"
    rule_name = "Price Above SMA120"
    ma_type = "sma"
    period = 120
    direction = "above"


def evaluate_ma0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0004."""
    return run_price_position_rule(MA0004PriceAboveSMA120Rule, df)
