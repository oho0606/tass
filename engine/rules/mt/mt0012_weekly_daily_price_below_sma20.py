"""MT0012 — Weekly Daily Price Below SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0012WeeklyDailyPriceBelowSMA20Rule(SpecRule):
    rule_id = "MT0012"
    rule_name = "Weekly Daily Price Below SMA20"


def evaluate_mt0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0012."""
    return run_spec_rule(MT0012WeeklyDailyPriceBelowSMA20Rule, df)
