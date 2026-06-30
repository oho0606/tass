"""TR0047 — Trend Duration Short. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0047TrendDurationShortRule(TrendSpecRule):
    rule_id = "TR0047"
    rule_name = "Trend Duration Short"


def evaluate_tr0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0047."""
    return run_trend_spec_rule(TR0047TrendDurationShortRule, df)
