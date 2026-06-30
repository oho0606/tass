"""EN0038 — Entry Close Below Reversal Bar Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0038EntryCloseBelowReversalBarLowRule(SpecRule):
    rule_id = "EN0038"
    rule_name = "Entry Close Below Reversal Bar Low"


def evaluate_en0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0038."""
    return run_spec_rule(EN0038EntryCloseBelowReversalBarLowRule, df)
