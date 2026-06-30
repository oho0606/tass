"""TR0056 — Trend Weakening. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0056TrendWeakeningRule(TrendSpecRule):
    rule_id = "TR0056"
    rule_name = "Trend Weakening"


def evaluate_tr0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0056."""
    return run_trend_spec_rule(TR0056TrendWeakeningRule, df)
