"""EN0033 — Entry Low At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0033EntryLowAtNPeriodLowRule(SpecRule):
    rule_id = "EN0033"
    rule_name = "Entry Low At N-Period Low"


def evaluate_en0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0033."""
    return run_spec_rule(EN0033EntryLowAtNPeriodLowRule, df)
