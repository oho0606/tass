"""TR0050 — Trend Age Increasing. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0050TrendAgeIncreasingRule(TrendSpecRule):
    rule_id = "TR0050"
    rule_name = "Trend Age Increasing"


def evaluate_tr0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0050."""
    return run_trend_spec_rule(TR0050TrendAgeIncreasingRule, df)
