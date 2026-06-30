"""PB0034 — Pullback Volume At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0034PullbackVolumeAtNPeriodLowRule(SpecRule):
    rule_id = "PB0034"
    rule_name = "Pullback Volume At N-Period Low"


def evaluate_pb0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0034."""
    return run_spec_rule(PB0034PullbackVolumeAtNPeriodLowRule, df)
