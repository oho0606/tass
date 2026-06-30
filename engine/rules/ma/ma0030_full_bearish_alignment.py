"""MA0030 — Full Bearish Alignment. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._alignment import FullAlignmentRule, run_alignment_rule, DEFAULT_PERIODS


class MA0030FullBearishAlignmentRule(FullAlignmentRule):
    rule_id = "MA0030"
    rule_name = "Full Bearish Alignment"
    direction = "bearish"
    periods = DEFAULT_PERIODS


def evaluate_ma0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0030."""
    return run_alignment_rule(MA0030FullBearishAlignmentRule, df)
