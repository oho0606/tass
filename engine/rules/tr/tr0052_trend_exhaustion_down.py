"""TR0052 — Trend Exhaustion Down. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0052TrendExhaustionDownRule(TrendSpecRule):
    rule_id = "TR0052"
    rule_name = "Trend Exhaustion Down"


def evaluate_tr0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0052."""
    return run_trend_spec_rule(TR0052TrendExhaustionDownRule, df)
