"""MT0041 — Weekly Daily 4H Trend Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0041WeeklyDaily4HTrendMatchRule(SpecRule):
    rule_id = "MT0041"
    rule_name = "Weekly Daily 4H Trend Match"


def evaluate_mt0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0041."""
    return run_spec_rule(MT0041WeeklyDaily4HTrendMatchRule, df)
