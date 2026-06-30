"""MA0058 — Dynamic Support Holding. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import DynamicLevelRule, run_structure_rule


class MA0058DynamicSupportHoldingRule(DynamicLevelRule):
    rule_id = "MA0058"
    rule_name = "Dynamic Support Holding"
    level = "support"


def evaluate_ma0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0058."""
    return run_structure_rule(MA0058DynamicSupportHoldingRule, df)
