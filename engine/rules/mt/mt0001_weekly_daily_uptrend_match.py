"""MT0001 — Weekly Daily Uptrend Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0001WeeklyDailyUptrendMatchRule(SpecRule):
    rule_id = "MT0001"
    rule_name = "Weekly Daily Uptrend Match"


def evaluate_mt0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0001."""
    return run_spec_rule(MT0001WeeklyDailyUptrendMatchRule, df)
