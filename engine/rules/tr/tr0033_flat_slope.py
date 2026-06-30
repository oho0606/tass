"""TR0033 — Flat Slope. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0033FlatSlopeRule(TrendSpecRule):
    rule_id = "TR0033"
    rule_name = "Flat Slope"


def evaluate_tr0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0033."""
    return run_trend_spec_rule(TR0033FlatSlopeRule, df)
