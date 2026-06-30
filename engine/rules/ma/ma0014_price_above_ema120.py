"""MA0014 — Price Above EMA120. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0014PriceAboveEMA120Rule(PricePositionRule):
    rule_id = "MA0014"
    rule_name = "Price Above EMA120"
    ma_type = "ema"
    period = 120
    direction = "above"


def evaluate_ma0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0014."""
    return run_price_position_rule(MA0014PriceAboveEMA120Rule, df)
