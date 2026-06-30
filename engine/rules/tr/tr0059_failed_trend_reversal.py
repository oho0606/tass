"""TR0059 — Failed Trend Reversal. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0059FailedTrendReversalRule(TrendSpecRule):
    rule_id = "TR0059"
    rule_name = "Failed Trend Reversal"


def evaluate_tr0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0059."""
    return run_trend_spec_rule(TR0059FailedTrendReversalRule, df)
