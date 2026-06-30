"""TR0080 — Trend Undefined. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0080TrendUndefinedRule(TrendSpecRule):
    rule_id = "TR0080"
    rule_name = "Trend Undefined"


def evaluate_tr0080(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0080."""
    return run_trend_spec_rule(TR0080TrendUndefinedRule, df)
