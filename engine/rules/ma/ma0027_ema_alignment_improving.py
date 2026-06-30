"""MA0027 — EMA Alignment Improving. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._alignment import AlignmentTrendRule, run_alignment_rule, DEFAULT_PERIODS


class MA0027EMAAlignmentImprovingRule(AlignmentTrendRule):
    rule_id = "MA0027"
    rule_name = "EMA Alignment Improving"
    ma_type = "ema"
    trend = "improving"
    periods = DEFAULT_PERIODS


def evaluate_ma0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0027."""
    return run_alignment_rule(MA0027EMAAlignmentImprovingRule, df)
