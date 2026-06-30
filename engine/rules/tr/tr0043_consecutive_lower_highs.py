"""TR0043 — Consecutive Lower Highs. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0043ConsecutiveLowerHighsRule(TrendSpecRule):
    rule_id = "TR0043"
    rule_name = "Consecutive Lower Highs"


def evaluate_tr0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0043."""
    return run_trend_spec_rule(TR0043ConsecutiveLowerHighsRule, df)
