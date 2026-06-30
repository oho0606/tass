"""PB0042 — Pullback Following Decline Leg. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0042PullbackFollowingDeclineLegRule(SpecRule):
    rule_id = "PB0042"
    rule_name = "Pullback Following Decline Leg"


def evaluate_pb0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0042."""
    return run_spec_rule(PB0042PullbackFollowingDeclineLegRule, df)
