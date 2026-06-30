"""MT0011 — Weekly Daily Price Above SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0011WeeklyDailyPriceAboveSMA20Rule(SpecRule):
    rule_id = "MT0011"
    rule_name = "Weekly Daily Price Above SMA20"


def evaluate_mt0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0011."""
    return run_spec_rule(MT0011WeeklyDailyPriceAboveSMA20Rule, df)
