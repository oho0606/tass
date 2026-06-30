"""MT0028 — Weekly Daily RSI Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0028WeeklyDailyRSIRisingRule(SpecRule):
    rule_id = "MT0028"
    rule_name = "Weekly Daily RSI Rising"


def evaluate_mt0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0028."""
    return run_spec_rule(MT0028WeeklyDailyRSIRisingRule, df)
