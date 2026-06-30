"""MA0048 — EMA Slope Decreasing. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaSlopeTrendRule, run_slope_rule


class MA0048EMASlopeDecreasingRule(MaSlopeTrendRule):
    rule_id = "MA0048"
    rule_name = "EMA Slope Decreasing"
    ma_type = "ema"
    trend = "decreasing"


def evaluate_ma0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0048."""
    return run_slope_rule(MA0048EMASlopeDecreasingRule, df)
