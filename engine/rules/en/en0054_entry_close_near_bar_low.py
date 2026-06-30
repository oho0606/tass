"""EN0054 — Entry Close Near Bar Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0054EntryCloseNearBarLowRule(SpecRule):
    rule_id = "EN0054"
    rule_name = "Entry Close Near Bar Low"


def evaluate_en0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0054."""
    return run_spec_rule(EN0054EntryCloseNearBarLowRule, df)
