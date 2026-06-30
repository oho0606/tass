"""MA0041 — SMA Rising. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaSlopeRule, run_slope_rule


class MA0041SMARisingRule(MaSlopeRule):
    rule_id = "MA0041"
    rule_name = "SMA Rising"
    ma_type = "sma"
    direction = "rising"


def evaluate_ma0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0041."""
    return run_slope_rule(MA0041SMARisingRule, df)
