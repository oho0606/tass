"""MT0022 — Weekly Daily RSI Below 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0022WeeklyDailyRSIBelow50Rule(SpecRule):
    rule_id = "MT0022"
    rule_name = "Weekly Daily RSI Below 50"


def evaluate_mt0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0022."""
    return run_spec_rule(MT0022WeeklyDailyRSIBelow50Rule, df)
