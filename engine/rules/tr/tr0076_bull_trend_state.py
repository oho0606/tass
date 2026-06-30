"""TR0076 — Bull Trend State. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0076BullTrendStateRule(TrendSpecRule):
    rule_id = "TR0076"
    rule_name = "Bull Trend State"


def evaluate_tr0076(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0076."""
    return run_trend_spec_rule(TR0076BullTrendStateRule, df)
