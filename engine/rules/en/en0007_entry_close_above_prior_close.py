"""EN0007 — Entry Close Above Prior Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0007EntryCloseAbovePriorCloseRule(SpecRule):
    rule_id = "EN0007"
    rule_name = "Entry Close Above Prior Close"


def evaluate_en0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0007."""
    return run_spec_rule(EN0007EntryCloseAbovePriorCloseRule, df)
