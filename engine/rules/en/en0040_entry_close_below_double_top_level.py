"""EN0040 — Entry Close Below Double Top Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0040EntryCloseBelowDoubleTopLevelRule(SpecRule):
    rule_id = "EN0040"
    rule_name = "Entry Close Below Double Top Level"


def evaluate_en0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0040."""
    return run_spec_rule(EN0040EntryCloseBelowDoubleTopLevelRule, df)
