"""EN0012 — Entry Close Below Prior Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0012EntryCloseBelowPriorSwingLowRule(SpecRule):
    rule_id = "EN0012"
    rule_name = "Entry Close Below Prior Swing Low"


def evaluate_en0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0012."""
    return run_spec_rule(EN0012EntryCloseBelowPriorSwingLowRule, df)
