"""MA0059 — Dynamic Resistance Holding. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import DynamicLevelRule, run_structure_rule


class MA0059DynamicResistanceHoldingRule(DynamicLevelRule):
    rule_id = "MA0059"
    rule_name = "Dynamic Resistance Holding"
    level = "resistance"


def evaluate_ma0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0059."""
    return run_structure_rule(MA0059DynamicResistanceHoldingRule, df)
