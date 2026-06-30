"""PB0041 — Pullback Following Advance Leg. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0041PullbackFollowingAdvanceLegRule(SpecRule):
    rule_id = "PB0041"
    rule_name = "Pullback Following Advance Leg"


def evaluate_pb0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0041."""
    return run_spec_rule(PB0041PullbackFollowingAdvanceLegRule, df)
