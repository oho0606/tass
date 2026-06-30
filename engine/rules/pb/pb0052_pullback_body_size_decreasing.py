"""PB0052 — Pullback Body Size Decreasing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0052PullbackBodySizeDecreasingRule(SpecRule):
    rule_id = "PB0052"
    rule_name = "Pullback Body Size Decreasing"


def evaluate_pb0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0052."""
    return run_spec_rule(PB0052PullbackBodySizeDecreasingRule, df)
