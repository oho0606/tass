"""TR0058 — Failed Trend Continuation. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0058FailedTrendContinuationRule(TrendSpecRule):
    rule_id = "TR0058"
    rule_name = "Failed Trend Continuation"


def evaluate_tr0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0058."""
    return run_trend_spec_rule(TR0058FailedTrendContinuationRule, df)
