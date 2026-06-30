"""PB0017 — Pullback Depth Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0017PullbackDepthAboveNPeriodAverageRule(SpecRule):
    rule_id = "PB0017"
    rule_name = "Pullback Depth Above N-Period Average"


def evaluate_pb0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0017."""
    return run_spec_rule(PB0017PullbackDepthAboveNPeriodAverageRule, df)
