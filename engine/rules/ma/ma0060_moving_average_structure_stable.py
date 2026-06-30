"""MA0060 — Moving Average Structure Stable. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import MaStructureStableRule, run_structure_rule


class MA0060MovingAverageStructureStableRule(MaStructureStableRule):
    rule_id = "MA0060"
    rule_name = "Moving Average Structure Stable"


def evaluate_ma0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0060."""
    return run_structure_rule(MA0060MovingAverageStructureStableRule, df)
