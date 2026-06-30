"""TR0077 — Bear Trend State. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0077BearTrendStateRule(TrendSpecRule):
    rule_id = "TR0077"
    rule_name = "Bear Trend State"


def evaluate_tr0077(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0077."""
    return run_trend_spec_rule(TR0077BearTrendStateRule, df)
