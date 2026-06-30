"""MA0047 — EMA Slope Increasing. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaSlopeTrendRule, run_slope_rule


class MA0047EMASlopeIncreasingRule(MaSlopeTrendRule):
    rule_id = "MA0047"
    rule_name = "EMA Slope Increasing"
    ma_type = "ema"
    trend = "increasing"


def evaluate_ma0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0047."""
    return run_slope_rule(MA0047EMASlopeIncreasingRule, df)
