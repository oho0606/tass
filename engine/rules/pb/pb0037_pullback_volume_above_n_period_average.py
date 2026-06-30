"""PB0037 — Pullback Volume Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0037PullbackVolumeAboveNPeriodAverageRule(SpecRule):
    rule_id = "PB0037"
    rule_name = "Pullback Volume Above N-Period Average"


def evaluate_pb0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0037."""
    return run_spec_rule(PB0037PullbackVolumeAboveNPeriodAverageRule, df)
