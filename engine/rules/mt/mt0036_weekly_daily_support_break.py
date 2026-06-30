"""MT0036 — Weekly Daily Support Break. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0036WeeklyDailySupportBreakRule(SpecRule):
    rule_id = "MT0036"
    rule_name = "Weekly Daily Support Break"


def evaluate_mt0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0036."""
    return run_spec_rule(MT0036WeeklyDailySupportBreakRule, df)
