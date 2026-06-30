"""MT0023 — Weekly RSI Above 50 Daily Below 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0023WeeklyRSIAbove50DailyBelow50Rule(SpecRule):
    rule_id = "MT0023"
    rule_name = "Weekly RSI Above 50 Daily Below 50"


def evaluate_mt0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0023."""
    return run_spec_rule(MT0023WeeklyRSIAbove50DailyBelow50Rule, df)
