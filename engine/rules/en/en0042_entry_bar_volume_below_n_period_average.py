"""EN0042 — Entry Bar Volume Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0042EntryBarVolumeBelowNPeriodAverageRule(SpecRule):
    rule_id = "EN0042"
    rule_name = "Entry Bar Volume Below N-Period Average"


def evaluate_en0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0042."""
    return run_spec_rule(EN0042EntryBarVolumeBelowNPeriodAverageRule, df)
