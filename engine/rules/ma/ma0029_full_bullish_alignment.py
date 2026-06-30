"""MA0029 — Full Bullish Alignment. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._alignment import FullAlignmentRule, run_alignment_rule, DEFAULT_PERIODS


class MA0029FullBullishAlignmentRule(FullAlignmentRule):
    rule_id = "MA0029"
    rule_name = "Full Bullish Alignment"
    direction = "bullish"
    periods = DEFAULT_PERIODS


def evaluate_ma0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0029."""
    return run_alignment_rule(MA0029FullBullishAlignmentRule, df)
