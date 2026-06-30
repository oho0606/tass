"""MA0055 — Moving Average Expansion. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import MaSpreadTrendRule, run_structure_rule


class MA0055MovingAverageExpansionRule(MaSpreadTrendRule):
    rule_id = "MA0055"
    rule_name = "Moving Average Expansion"
    trend = "expansion"


def evaluate_ma0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0055."""
    return run_structure_rule(MA0055MovingAverageExpansionRule, df)
