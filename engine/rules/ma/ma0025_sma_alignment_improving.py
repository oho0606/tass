"""MA0025 — SMA Alignment Improving. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._alignment import AlignmentTrendRule, run_alignment_rule, DEFAULT_PERIODS


class MA0025SMAAlignmentImprovingRule(AlignmentTrendRule):
    rule_id = "MA0025"
    rule_name = "SMA Alignment Improving"
    ma_type = "sma"
    trend = "improving"
    periods = DEFAULT_PERIODS


def evaluate_ma0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0025."""
    return run_alignment_rule(MA0025SMAAlignmentImprovingRule, df)
