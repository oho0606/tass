"""MR0016 — SMA20 Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0016SMA20FallingRule(SpecRule):
    rule_id = "MR0016"
    rule_name = "SMA20 Falling"


def evaluate_mr0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0016."""
    return run_spec_rule(MR0016SMA20FallingRule, df)
