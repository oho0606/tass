"""MT0024 — Weekly Daily MACD Above Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0024WeeklyDailyMACDAboveZeroRule(SpecRule):
    rule_id = "MT0024"
    rule_name = "Weekly Daily MACD Above Zero"


def evaluate_mt0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0024."""
    return run_spec_rule(MT0024WeeklyDailyMACDAboveZeroRule, df)
