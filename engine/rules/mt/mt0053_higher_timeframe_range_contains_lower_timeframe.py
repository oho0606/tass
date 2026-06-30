"""MT0053 — Higher Timeframe Range Contains Lower Timeframe. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0053HigherTimeframeRangeContainsLowerTimeframeRule(SpecRule):
    rule_id = "MT0053"
    rule_name = "Higher Timeframe Range Contains Lower Timeframe"


def evaluate_mt0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0053."""
    return run_spec_rule(MT0053HigherTimeframeRangeContainsLowerTimeframeRule, df)
