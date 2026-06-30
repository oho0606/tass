"""EN0008 — Entry Close Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0008EntryCloseAboveNPeriodHighRule(SpecRule):
    rule_id = "EN0008"
    rule_name = "Entry Close Above N-Period High"


def evaluate_en0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0008."""
    return run_spec_rule(EN0008EntryCloseAboveNPeriodHighRule, df)
