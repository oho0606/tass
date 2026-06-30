"""MT0034 — Weekly Daily Swing Low Break. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0034WeeklyDailySwingLowBreakRule(SpecRule):
    rule_id = "MT0034"
    rule_name = "Weekly Daily Swing Low Break"


def evaluate_mt0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0034."""
    return run_spec_rule(MT0034WeeklyDailySwingLowBreakRule, df)
