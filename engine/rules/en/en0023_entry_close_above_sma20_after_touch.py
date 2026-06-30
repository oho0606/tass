"""EN0023 — Entry Close Above SMA20 After Touch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0023EntryCloseAboveSMA20AfterTouchRule(SpecRule):
    rule_id = "EN0023"
    rule_name = "Entry Close Above SMA20 After Touch"


def evaluate_en0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0023."""
    return run_spec_rule(EN0023EntryCloseAboveSMA20AfterTouchRule, df)
