"""PB0009 — Pullback Close Above Prior Leg Midpoint. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0009PullbackCloseAbovePriorLegMidpointRule(SpecRule):
    rule_id = "PB0009"
    rule_name = "Pullback Close Above Prior Leg Midpoint"


def evaluate_pb0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0009."""
    return run_spec_rule(PB0009PullbackCloseAbovePriorLegMidpointRule, df)
