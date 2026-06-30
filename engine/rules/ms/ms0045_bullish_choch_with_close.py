"""MS0045 — Bullish CHoCH With Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0045BullishCHoCHWithCloseRule(SpecRule):
    rule_id = "MS0045"
    rule_name = "Bullish CHoCH With Close"


def evaluate_ms0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0045."""
    return run_spec_rule(MS0045BullishCHoCHWithCloseRule, df)
