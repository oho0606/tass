"""MS0036 — Bearish BOS With Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0036BearishBOSWithCloseRule(SpecRule):
    rule_id = "MS0036"
    rule_name = "Bearish BOS With Close"


def evaluate_ms0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0036."""
    return run_spec_rule(MS0036BearishBOSWithCloseRule, df)
