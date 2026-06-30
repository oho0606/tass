"""MS0035 — Bullish BOS With Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0035BullishBOSWithCloseRule(SpecRule):
    rule_id = "MS0035"
    rule_name = "Bullish BOS With Close"


def evaluate_ms0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0035."""
    return run_spec_rule(MS0035BullishBOSWithCloseRule, df)
