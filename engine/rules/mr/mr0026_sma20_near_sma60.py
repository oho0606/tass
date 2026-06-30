"""MR0026 — SMA20 Near SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0026SMA20NearSMA60Rule(SpecRule):
    rule_id = "MR0026"
    rule_name = "SMA20 Near SMA60"


def evaluate_mr0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0026."""
    return run_spec_rule(MR0026SMA20NearSMA60Rule, df)
