"""TR0006 — Downtrend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0006DowntrendRule(TrendSpecRule):
    rule_id = "TR0006"
    rule_name = "Downtrend"


def evaluate_tr0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0006."""
    return run_trend_spec_rule(TR0006DowntrendRule, df)
