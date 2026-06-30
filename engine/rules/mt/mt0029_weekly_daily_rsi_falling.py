"""MT0029 — Weekly Daily RSI Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0029WeeklyDailyRSIFallingRule(SpecRule):
    rule_id = "MT0029"
    rule_name = "Weekly Daily RSI Falling"


def evaluate_mt0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0029."""
    return run_spec_rule(MT0029WeeklyDailyRSIFallingRule, df)
