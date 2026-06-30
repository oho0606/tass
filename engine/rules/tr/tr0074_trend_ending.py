"""TR0074 — Trend Ending. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0074TrendEndingRule(TrendSpecRule):
    rule_id = "TR0074"
    rule_name = "Trend Ending"


def evaluate_tr0074(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0074."""
    return run_trend_spec_rule(TR0074TrendEndingRule, df)
