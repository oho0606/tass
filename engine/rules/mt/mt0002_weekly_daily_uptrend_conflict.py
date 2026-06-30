"""MT0002 — Weekly Daily Uptrend Conflict. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0002WeeklyDailyUptrendConflictRule(SpecRule):
    rule_id = "MT0002"
    rule_name = "Weekly Daily Uptrend Conflict"


def evaluate_mt0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0002."""
    return run_spec_rule(MT0002WeeklyDailyUptrendConflictRule, df)
