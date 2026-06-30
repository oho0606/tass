"""MA0043 — EMA Rising. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaSlopeRule, run_slope_rule


class MA0043EMARisingRule(MaSlopeRule):
    rule_id = "MA0043"
    rule_name = "EMA Rising"
    ma_type = "ema"
    direction = "rising"


def evaluate_ma0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0043."""
    return run_slope_rule(MA0043EMARisingRule, df)
