"""MT0039 — Weekly Breakout Confirmed By Daily Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0039WeeklyBreakoutConfirmedByDailyCloseRule(SpecRule):
    rule_id = "MT0039"
    rule_name = "Weekly Breakout Confirmed By Daily Close"


def evaluate_mt0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0039."""
    return run_spec_rule(MT0039WeeklyBreakoutConfirmedByDailyCloseRule, df)
