"""EN0041 — Entry Bar Volume Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0041EntryBarVolumeAboveNPeriodAverageRule(SpecRule):
    rule_id = "EN0041"
    rule_name = "Entry Bar Volume Above N-Period Average"


def evaluate_en0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0041."""
    return run_spec_rule(EN0041EntryBarVolumeAboveNPeriodAverageRule, df)
