"""BO0043 — High Above Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0043HighAboveHorizontalResistanceRule(SpecRule):
    rule_id = "BO0043"
    rule_name = "High Above Horizontal Resistance"


def evaluate_bo0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0043."""
    return run_spec_rule(BO0043HighAboveHorizontalResistanceRule, df)
