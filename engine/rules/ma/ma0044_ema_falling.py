"""MA0044 — EMA Falling. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaSlopeRule, run_slope_rule


class MA0044EMAFallingRule(MaSlopeRule):
    rule_id = "MA0044"
    rule_name = "EMA Falling"
    ma_type = "ema"
    direction = "falling"


def evaluate_ma0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0044."""
    return run_slope_rule(MA0044EMAFallingRule, df)
