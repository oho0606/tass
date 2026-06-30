"""MA0045 — SMA Slope Increasing. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaSlopeTrendRule, run_slope_rule


class MA0045SMASlopeIncreasingRule(MaSlopeTrendRule):
    rule_id = "MA0045"
    rule_name = "SMA Slope Increasing"
    ma_type = "sma"
    trend = "increasing"


def evaluate_ma0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0045."""
    return run_slope_rule(MA0045SMASlopeIncreasingRule, df)
