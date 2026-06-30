"""MA0052 — Price Extended Below MA. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import PriceDistanceRule, run_structure_rule


class MA0052PriceExtendedBelowMARule(PriceDistanceRule):
    rule_id = "MA0052"
    rule_name = "Price Extended Below MA"
    mode = "extended_below"


def evaluate_ma0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0052."""
    return run_structure_rule(MA0052PriceExtendedBelowMARule, df)
