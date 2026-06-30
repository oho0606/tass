"""PB0051 — Pullback Overlapping Prior Bars. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0051PullbackOverlappingPriorBarsRule(SpecRule):
    rule_id = "PB0051"
    rule_name = "Pullback Overlapping Prior Bars"


def evaluate_pb0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0051."""
    return run_spec_rule(PB0051PullbackOverlappingPriorBarsRule, df)
