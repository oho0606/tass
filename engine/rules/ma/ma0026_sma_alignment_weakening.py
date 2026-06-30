"""MA0026 — SMA Alignment Weakening. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._alignment import AlignmentTrendRule, run_alignment_rule, DEFAULT_PERIODS


class MA0026SMAAlignmentWeakeningRule(AlignmentTrendRule):
    rule_id = "MA0026"
    rule_name = "SMA Alignment Weakening"
    ma_type = "sma"
    trend = "weakening"
    periods = DEFAULT_PERIODS


def evaluate_ma0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0026."""
    return run_alignment_rule(MA0026SMAAlignmentWeakeningRule, df)
