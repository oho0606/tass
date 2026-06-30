"""MT0025 — Weekly Daily MACD Below Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0025WeeklyDailyMACDBelowZeroRule(SpecRule):
    rule_id = "MT0025"
    rule_name = "Weekly Daily MACD Below Zero"


def evaluate_mt0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0025."""
    return run_spec_rule(MT0025WeeklyDailyMACDBelowZeroRule, df)
