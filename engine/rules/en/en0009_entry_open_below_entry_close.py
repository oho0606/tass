"""EN0009 — Entry Open Below Entry Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0009EntryOpenBelowEntryCloseRule(SpecRule):
    rule_id = "EN0009"
    rule_name = "Entry Open Below Entry Close"


def evaluate_en0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0009."""
    return run_spec_rule(EN0009EntryOpenBelowEntryCloseRule, df)
