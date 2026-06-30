"""MT0052 — Weekly Trend Opposes Daily Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0052WeeklyTrendOpposesDailyTrendRule(SpecRule):
    rule_id = "MT0052"
    rule_name = "Weekly Trend Opposes Daily Trend"


def evaluate_mt0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0052."""
    return run_spec_rule(MT0052WeeklyTrendOpposesDailyTrendRule, df)
