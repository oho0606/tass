"""MA0056 — Moving Average Convergence. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import MaSpreadLevelRule, run_structure_rule


class MA0056MovingAverageConvergenceRule(MaSpreadLevelRule):
    rule_id = "MA0056"
    rule_name = "Moving Average Convergence"
    level = "convergence"


def evaluate_ma0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0056."""
    return run_structure_rule(MA0056MovingAverageConvergenceRule, df)
