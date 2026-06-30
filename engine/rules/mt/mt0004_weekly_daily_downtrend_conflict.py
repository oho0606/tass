"""MT0004 — Weekly Daily Downtrend Conflict. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0004WeeklyDailyDowntrendConflictRule(SpecRule):
    rule_id = "MT0004"
    rule_name = "Weekly Daily Downtrend Conflict"


def evaluate_mt0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0004."""
    return run_spec_rule(MT0004WeeklyDailyDowntrendConflictRule, df)
