"""MA0042 — SMA Falling. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaSlopeRule, run_slope_rule


class MA0042SMAFallingRule(MaSlopeRule):
    rule_id = "MA0042"
    rule_name = "SMA Falling"
    ma_type = "sma"
    direction = "falling"


def evaluate_ma0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0042."""
    return run_slope_rule(MA0042SMAFallingRule, df)
