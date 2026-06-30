"""BO0041 — Close Above Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0041CloseAboveHorizontalResistanceRule(SpecRule):
    rule_id = "BO0041"
    rule_name = "Close Above Horizontal Resistance"


def evaluate_bo0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0041."""
    return run_spec_rule(BO0041CloseAboveHorizontalResistanceRule, df)
