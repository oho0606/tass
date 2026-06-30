"""MA0051 — Price Extended Above MA. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import PriceDistanceRule, run_structure_rule


class MA0051PriceExtendedAboveMARule(PriceDistanceRule):
    rule_id = "MA0051"
    rule_name = "Price Extended Above MA"
    mode = "extended_above"


def evaluate_ma0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0051."""
    return run_structure_rule(MA0051PriceExtendedAboveMARule, df)
