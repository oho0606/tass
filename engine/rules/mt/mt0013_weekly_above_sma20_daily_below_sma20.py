"""MT0013 — Weekly Above SMA20 Daily Below SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0013WeeklyAboveSMA20DailyBelowSMA20Rule(SpecRule):
    rule_id = "MT0013"
    rule_name = "Weekly Above SMA20 Daily Below SMA20"


def evaluate_mt0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0013."""
    return run_spec_rule(MT0013WeeklyAboveSMA20DailyBelowSMA20Rule, df)
