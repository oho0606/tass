"""PB0032 — Pullback Volume Decreasing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0032PullbackVolumeDecreasingRule(SpecRule):
    rule_id = "PB0032"
    rule_name = "Pullback Volume Decreasing"


def evaluate_pb0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0032."""
    return run_spec_rule(PB0032PullbackVolumeDecreasingRule, df)
