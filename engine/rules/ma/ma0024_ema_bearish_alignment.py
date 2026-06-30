"""MA0024 — EMA Bearish Alignment. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._alignment import AlignmentRule, run_alignment_rule, DEFAULT_PERIODS


class MA0024EMABearishAlignmentRule(AlignmentRule):
    rule_id = "MA0024"
    rule_name = "EMA Bearish Alignment"
    ma_type = "ema"
    direction = "bearish"
    periods = DEFAULT_PERIODS


def evaluate_ma0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0024."""
    return run_alignment_rule(MA0024EMABearishAlignmentRule, df)
