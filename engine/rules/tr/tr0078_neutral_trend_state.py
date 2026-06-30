"""TR0078 — Neutral Trend State. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0078NeutralTrendStateRule(TrendSpecRule):
    rule_id = "TR0078"
    rule_name = "Neutral Trend State"


def evaluate_tr0078(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0078."""
    return run_trend_spec_rule(TR0078NeutralTrendStateRule, df)
