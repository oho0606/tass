"""MT0051 — Weekly Trend Supports Daily Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0051WeeklyTrendSupportsDailyTrendRule(SpecRule):
    rule_id = "MT0051"
    rule_name = "Weekly Trend Supports Daily Trend"


def evaluate_mt0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0051."""
    return run_spec_rule(MT0051WeeklyTrendSupportsDailyTrendRule, df)
