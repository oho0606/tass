"""MA0022 — SMA Bearish Alignment. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._alignment import AlignmentRule, run_alignment_rule, DEFAULT_PERIODS


class MA0022SMABearishAlignmentRule(AlignmentRule):
    rule_id = "MA0022"
    rule_name = "SMA Bearish Alignment"
    ma_type = "sma"
    direction = "bearish"
    periods = DEFAULT_PERIODS


def evaluate_ma0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0022."""
    return run_alignment_rule(MA0022SMABearishAlignmentRule, df)
