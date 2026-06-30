"""MA0028 — EMA Alignment Weakening. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._alignment import AlignmentTrendRule, run_alignment_rule, DEFAULT_PERIODS


class MA0028EMAAlignmentWeakeningRule(AlignmentTrendRule):
    rule_id = "MA0028"
    rule_name = "EMA Alignment Weakening"
    ma_type = "ema"
    trend = "weakening"
    periods = DEFAULT_PERIODS


def evaluate_ma0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0028."""
    return run_alignment_rule(MA0028EMAAlignmentWeakeningRule, df)
