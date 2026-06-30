"""TR0012 — Weak Uptrend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0012WeakUptrendRule(TrendSpecRule):
    rule_id = "TR0012"
    rule_name = "Weak Uptrend"


def evaluate_tr0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0012."""
    return run_trend_spec_rule(TR0012WeakUptrendRule, df)
