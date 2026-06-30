"""MT0017 — Weekly Daily SMA Bullish Alignment. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0017WeeklyDailySMABullishAlignmentRule(SpecRule):
    rule_id = "MT0017"
    rule_name = "Weekly Daily SMA Bullish Alignment"


def evaluate_mt0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0017."""
    return run_spec_rule(MT0017WeeklyDailySMABullishAlignmentRule, df)
