"""PB0060 — Pullback Candle Count Decreasing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0060PullbackCandleCountDecreasingRule(SpecRule):
    rule_id = "PB0060"
    rule_name = "Pullback Candle Count Decreasing"


def evaluate_pb0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0060."""
    return run_spec_rule(PB0060PullbackCandleCountDecreasingRule, df)
