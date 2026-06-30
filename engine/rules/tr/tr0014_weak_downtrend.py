"""TR0014 — Weak Downtrend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0014WeakDowntrendRule(TrendSpecRule):
    rule_id = "TR0014"
    rule_name = "Weak Downtrend"


def evaluate_tr0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0014."""
    return run_trend_spec_rule(TR0014WeakDowntrendRule, df)
