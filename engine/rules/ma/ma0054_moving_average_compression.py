"""MA0054 — Moving Average Compression. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import MaSpreadTrendRule, run_structure_rule


class MA0054MovingAverageCompressionRule(MaSpreadTrendRule):
    rule_id = "MA0054"
    rule_name = "Moving Average Compression"
    trend = "compression"


def evaluate_ma0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0054."""
    return run_structure_rule(MA0054MovingAverageCompressionRule, df)
