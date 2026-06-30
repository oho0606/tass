"""MT0054 — Lower Timeframe Range Extends Beyond Higher Timeframe. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0054LowerTimeframeRangeExtendsBeyondHigherTimeframeRule(SpecRule):
    rule_id = "MT0054"
    rule_name = "Lower Timeframe Range Extends Beyond Higher Timeframe"


def evaluate_mt0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0054."""
    return run_spec_rule(MT0054LowerTimeframeRangeExtendsBeyondHigherTimeframeRule, df)
