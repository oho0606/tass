"""TR0045 — Trend Persistence High. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0045TrendPersistenceHighRule(TrendSpecRule):
    rule_id = "TR0045"
    rule_name = "Trend Persistence High"


def evaluate_tr0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0045."""
    return run_trend_spec_rule(TR0045TrendPersistenceHighRule, df)
