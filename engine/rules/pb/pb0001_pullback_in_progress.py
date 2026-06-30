"""PB0001 — Pullback In Progress. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0001PullbackInProgressRule(SpecRule):
    rule_id = "PB0001"
    rule_name = "Pullback In Progress"


def evaluate_pb0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0001."""
    return run_spec_rule(PB0001PullbackInProgressRule, df)
