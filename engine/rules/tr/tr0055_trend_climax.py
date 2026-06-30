"""TR0055 — Trend Climax. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0055TrendClimaxRule(TrendSpecRule):
    rule_id = "TR0055"
    rule_name = "Trend Climax"


def evaluate_tr0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0055."""
    return run_trend_spec_rule(TR0055TrendClimaxRule, df)
