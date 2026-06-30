"""MT0018 — Weekly Daily SMA Bearish Alignment. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0018WeeklyDailySMABearishAlignmentRule(SpecRule):
    rule_id = "MT0018"
    rule_name = "Weekly Daily SMA Bearish Alignment"


def evaluate_mt0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0018."""
    return run_spec_rule(MT0018WeeklyDailySMABearishAlignmentRule, df)
