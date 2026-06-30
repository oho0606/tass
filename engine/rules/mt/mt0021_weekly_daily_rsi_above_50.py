"""MT0021 — Weekly Daily RSI Above 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0021WeeklyDailyRSIAbove50Rule(SpecRule):
    rule_id = "MT0021"
    rule_name = "Weekly Daily RSI Above 50"


def evaluate_mt0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0021."""
    return run_spec_rule(MT0021WeeklyDailyRSIAbove50Rule, df)
