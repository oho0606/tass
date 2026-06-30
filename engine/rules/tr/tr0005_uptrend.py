"""TR0005 — Uptrend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0005UptrendRule(TrendSpecRule):
    rule_id = "TR0005"
    rule_name = "Uptrend"


def evaluate_tr0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0005."""
    return run_trend_spec_rule(TR0005UptrendRule, df)
