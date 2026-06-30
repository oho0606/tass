"""EN0015 — Entry Close Above 52-Week High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0015EntryCloseAbove52WeekHighRule(SpecRule):
    rule_id = "EN0015"
    rule_name = "Entry Close Above 52-Week High"


def evaluate_en0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0015."""
    return run_spec_rule(EN0015EntryCloseAbove52WeekHighRule, df)
