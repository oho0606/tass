"""TR0051 — Trend Exhaustion Up. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0051TrendExhaustionUpRule(TrendSpecRule):
    rule_id = "TR0051"
    rule_name = "Trend Exhaustion Up"


def evaluate_tr0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0051."""
    return run_trend_spec_rule(TR0051TrendExhaustionUpRule, df)
