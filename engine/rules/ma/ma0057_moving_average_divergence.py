"""MA0057 — Moving Average Divergence. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import MaSpreadLevelRule, run_structure_rule


class MA0057MovingAverageDivergenceRule(MaSpreadLevelRule):
    rule_id = "MA0057"
    rule_name = "Moving Average Divergence"
    level = "divergence"


def evaluate_ma0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0057."""
    return run_structure_rule(MA0057MovingAverageDivergenceRule, df)
