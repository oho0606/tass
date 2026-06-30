"""TR0057 — Trend Failure. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0057TrendFailureRule(TrendSpecRule):
    rule_id = "TR0057"
    rule_name = "Trend Failure"


def evaluate_tr0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0057."""
    return run_trend_spec_rule(TR0057TrendFailureRule, df)
