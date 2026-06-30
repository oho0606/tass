"""MA0053 — Price Near Moving Average. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import PriceDistanceRule, run_structure_rule


class MA0053PriceNearMovingAverageRule(PriceDistanceRule):
    rule_id = "MA0053"
    rule_name = "Price Near Moving Average"
    mode = "near"


def evaluate_ma0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0053."""
    return run_structure_rule(MA0053PriceNearMovingAverageRule, df)
