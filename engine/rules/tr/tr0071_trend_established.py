"""TR0071 — Trend Established. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0071TrendEstablishedRule(TrendSpecRule):
    rule_id = "TR0071"
    rule_name = "Trend Established"


def evaluate_tr0071(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0071."""
    return run_trend_spec_rule(TR0071TrendEstablishedRule, df)
