"""TR0030 — Trend Integrity. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0030TrendIntegrityRule(TrendSpecRule):
    rule_id = "TR0030"
    rule_name = "Trend Integrity"


def evaluate_tr0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0030."""
    return run_trend_spec_rule(TR0030TrendIntegrityRule, df)
