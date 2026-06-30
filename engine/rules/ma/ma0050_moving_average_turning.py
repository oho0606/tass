"""MA0050 — Moving Average Turning. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaTurningRule, run_slope_rule


class MA0050MovingAverageTurningRule(MaTurningRule):
    rule_id = "MA0050"
    rule_name = "Moving Average Turning"


def evaluate_ma0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0050."""
    return run_slope_rule(MA0050MovingAverageTurningRule, df)
