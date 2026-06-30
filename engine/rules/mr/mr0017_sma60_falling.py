"""MR0017 — SMA60 Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0017SMA60FallingRule(SpecRule):
    rule_id = "MR0017"
    rule_name = "SMA60 Falling"


def evaluate_mr0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0017."""
    return run_spec_rule(MR0017SMA60FallingRule, df)
