"""MT0040 — Daily Breakout Rejected By Weekly Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0040DailyBreakoutRejectedByWeeklyCloseRule(SpecRule):
    rule_id = "MT0040"
    rule_name = "Daily Breakout Rejected By Weekly Close"


def evaluate_mt0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0040."""
    return run_spec_rule(MT0040DailyBreakoutRejectedByWeeklyCloseRule, df)
