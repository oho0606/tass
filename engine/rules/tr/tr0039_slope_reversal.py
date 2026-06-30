"""TR0039 — Slope Reversal. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0039SlopeReversalRule(TrendSpecRule):
    rule_id = "TR0039"
    rule_name = "Slope Reversal"


def evaluate_tr0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0039."""
    return run_trend_spec_rule(TR0039SlopeReversalRule, df)
