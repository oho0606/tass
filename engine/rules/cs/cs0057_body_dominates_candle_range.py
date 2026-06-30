"""CS0057 — Body Dominates Candle Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0057BodyDominatesCandleRangeRule(SpecRule):
    rule_id = "CS0057"
    rule_name = "Body Dominates Candle Range"


def evaluate_cs0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0057."""
    return run_spec_rule(CS0057BodyDominatesCandleRangeRule, df)
