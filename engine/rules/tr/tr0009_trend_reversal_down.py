"""TR0009 — Trend Reversal Down. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0009TrendReversalDownRule(TrendSpecRule):
    rule_id = "TR0009"
    rule_name = "Trend Reversal Down"


def evaluate_tr0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0009."""
    return run_trend_spec_rule(TR0009TrendReversalDownRule, df)
