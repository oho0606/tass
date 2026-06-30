"""MT0045 — Higher Timeframe Trend Matches Lower Timeframe. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0045HigherTimeframeTrendMatchesLowerTimeframeRule(SpecRule):
    rule_id = "MT0045"
    rule_name = "Higher Timeframe Trend Matches Lower Timeframe"


def evaluate_mt0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0045."""
    return run_spec_rule(MT0045HigherTimeframeTrendMatchesLowerTimeframeRule, df)
