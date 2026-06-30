"""TR0054 — Selling Exhaustion. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0054SellingExhaustionRule(TrendSpecRule):
    rule_id = "TR0054"
    rule_name = "Selling Exhaustion"


def evaluate_tr0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0054."""
    return run_trend_spec_rule(TR0054SellingExhaustionRule, df)
