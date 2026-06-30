"""MA0003 — Price Above SMA60. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class MA0003PriceAboveSMA60Rule(PricePositionRule):
    rule_id = "MA0003"
    rule_name = "Price Above SMA60"
    ma_type = "sma"
    period = 60
    direction = "above"


def evaluate_ma0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0003."""
    return run_price_position_rule(MA0003PriceAboveSMA60Rule, df)
