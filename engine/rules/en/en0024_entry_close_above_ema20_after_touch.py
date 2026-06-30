"""EN0024 — Entry Close Above EMA20 After Touch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0024EntryCloseAboveEMA20AfterTouchRule(SpecRule):
    rule_id = "EN0024"
    rule_name = "Entry Close Above EMA20 After Touch"


def evaluate_en0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0024."""
    return run_spec_rule(EN0024EntryCloseAboveEMA20AfterTouchRule, df)
