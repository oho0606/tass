"""TR0046 — Trend Persistence Low. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0046TrendPersistenceLowRule(TrendSpecRule):
    rule_id = "TR0046"
    rule_name = "Trend Persistence Low"


def evaluate_tr0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0046."""
    return run_trend_spec_rule(TR0046TrendPersistenceLowRule, df)
