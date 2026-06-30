"""TR0015 — ADX Rising. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0015ADXRisingRule(TrendSpecRule):
    rule_id = "TR0015"
    rule_name = "ADX Rising"


def evaluate_tr0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0015."""
    return run_trend_spec_rule(TR0015ADXRisingRule, df)
