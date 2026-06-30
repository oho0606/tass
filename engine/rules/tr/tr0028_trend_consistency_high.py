"""TR0028 — Trend Consistency High. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0028TrendConsistencyHighRule(TrendSpecRule):
    rule_id = "TR0028"
    rule_name = "Trend Consistency High"


def evaluate_tr0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0028."""
    return run_trend_spec_rule(TR0028TrendConsistencyHighRule, df)
