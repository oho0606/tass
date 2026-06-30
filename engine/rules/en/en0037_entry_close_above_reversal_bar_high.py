"""EN0037 — Entry Close Above Reversal Bar High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0037EntryCloseAboveReversalBarHighRule(SpecRule):
    rule_id = "EN0037"
    rule_name = "Entry Close Above Reversal Bar High"


def evaluate_en0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0037."""
    return run_spec_rule(EN0037EntryCloseAboveReversalBarHighRule, df)
