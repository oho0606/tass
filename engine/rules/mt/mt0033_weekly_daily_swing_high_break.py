"""MT0033 — Weekly Daily Swing High Break. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0033WeeklyDailySwingHighBreakRule(SpecRule):
    rule_id = "MT0033"
    rule_name = "Weekly Daily Swing High Break"


def evaluate_mt0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0033."""
    return run_spec_rule(MT0033WeeklyDailySwingHighBreakRule, df)
