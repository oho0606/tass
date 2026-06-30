"""MA0046 — SMA Slope Decreasing. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaSlopeTrendRule, run_slope_rule


class MA0046SMASlopeDecreasingRule(MaSlopeTrendRule):
    rule_id = "MA0046"
    rule_name = "SMA Slope Decreasing"
    ma_type = "sma"
    trend = "decreasing"


def evaluate_ma0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0046."""
    return run_slope_rule(MA0046SMASlopeDecreasingRule, df)
