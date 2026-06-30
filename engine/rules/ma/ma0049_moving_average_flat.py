"""MA0049 — Moving Average Flat. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import MaFlatRule, run_slope_rule


class MA0049MovingAverageFlatRule(MaFlatRule):
    rule_id = "MA0049"
    rule_name = "Moving Average Flat"


def evaluate_ma0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0049."""
    return run_slope_rule(MA0049MovingAverageFlatRule, df)
