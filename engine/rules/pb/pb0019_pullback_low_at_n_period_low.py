"""PB0019 — Pullback Low At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0019PullbackLowAtNPeriodLowRule(SpecRule):
    rule_id = "PB0019"
    rule_name = "Pullback Low At N-Period Low"


def evaluate_pb0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0019."""
    return run_spec_rule(PB0019PullbackLowAtNPeriodLowRule, df)
