"""TR0070 — Trend Confirmation Restored. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0070TrendConfirmationRestoredRule(TrendSpecRule):
    rule_id = "TR0070"
    rule_name = "Trend Confirmation Restored"


def evaluate_tr0070(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0070."""
    return run_trend_spec_rule(TR0070TrendConfirmationRestoredRule, df)
