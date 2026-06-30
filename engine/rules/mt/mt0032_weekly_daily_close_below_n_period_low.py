"""MT0032 — Weekly Daily Close Below N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0032WeeklyDailyCloseBelowNPeriodLowRule(SpecRule):
    rule_id = "MT0032"
    rule_name = "Weekly Daily Close Below N-Period Low"


def evaluate_mt0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0032."""
    return run_spec_rule(MT0032WeeklyDailyCloseBelowNPeriodLowRule, df)
