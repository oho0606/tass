"""TR0016 — ADX Falling. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0016ADXFallingRule(TrendSpecRule):
    rule_id = "TR0016"
    rule_name = "ADX Falling"


def evaluate_tr0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0016."""
    return run_trend_spec_rule(TR0016ADXFallingRule, df)
