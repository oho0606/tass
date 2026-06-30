"""MR0002 — Close Above SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0002CloseAboveSMA60Rule(SpecRule):
    rule_id = "MR0002"
    rule_name = "Close Above SMA60"


def evaluate_mr0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0002."""
    return run_spec_rule(MR0002CloseAboveSMA60Rule, df)
