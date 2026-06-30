"""TR0010 — Trend Continuation. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0010TrendContinuationRule(TrendSpecRule):
    rule_id = "TR0010"
    rule_name = "Trend Continuation"


def evaluate_tr0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0010."""
    return run_trend_spec_rule(TR0010TrendContinuationRule, df)
