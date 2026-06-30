"""TR0029 — Trend Consistency Low. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0029TrendConsistencyLowRule(TrendSpecRule):
    rule_id = "TR0029"
    rule_name = "Trend Consistency Low"


def evaluate_tr0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0029."""
    return run_trend_spec_rule(TR0029TrendConsistencyLowRule, df)
