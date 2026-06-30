"""TR0027 — Unstable Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0027UnstableTrendRule(TrendSpecRule):
    rule_id = "TR0027"
    rule_name = "Unstable Trend"


def evaluate_tr0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0027."""
    return run_trend_spec_rule(TR0027UnstableTrendRule, df)
