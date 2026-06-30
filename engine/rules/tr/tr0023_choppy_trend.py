"""TR0023 — Choppy Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0023ChoppyTrendRule(TrendSpecRule):
    rule_id = "TR0023"
    rule_name = "Choppy Trend"


def evaluate_tr0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0023."""
    return run_trend_spec_rule(TR0023ChoppyTrendRule, df)
