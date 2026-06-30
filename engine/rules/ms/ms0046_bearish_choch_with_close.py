"""MS0046 — Bearish CHoCH With Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0046BearishCHoCHWithCloseRule(SpecRule):
    rule_id = "MS0046"
    rule_name = "Bearish CHoCH With Close"


def evaluate_ms0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0046."""
    return run_spec_rule(MS0046BearishCHoCHWithCloseRule, df)
