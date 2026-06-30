"""MA0023 — EMA Bullish Alignment. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._alignment import AlignmentRule, run_alignment_rule, DEFAULT_PERIODS


class MA0023EMABullishAlignmentRule(AlignmentRule):
    rule_id = "MA0023"
    rule_name = "EMA Bullish Alignment"
    ma_type = "ema"
    direction = "bullish"
    periods = DEFAULT_PERIODS


def evaluate_ma0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0023."""
    return run_alignment_rule(MA0023EMABullishAlignmentRule, df)
