"""PB0018 — Price Below 50 Percent Retracement Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0018PriceBelow50PercentRetracementLevelRule(SpecRule):
    rule_id = "PB0018"
    rule_name = "Price Below 50 Percent Retracement Level"


def evaluate_pb0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0018."""
    return run_spec_rule(PB0018PriceBelow50PercentRetracementLevelRule, df)
