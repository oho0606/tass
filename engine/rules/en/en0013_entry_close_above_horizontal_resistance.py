"""EN0013 — Entry Close Above Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0013EntryCloseAboveHorizontalResistanceRule(SpecRule):
    rule_id = "EN0013"
    rule_name = "Entry Close Above Horizontal Resistance"


def evaluate_en0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0013."""
    return run_spec_rule(EN0013EntryCloseAboveHorizontalResistanceRule, df)
