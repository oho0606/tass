"""EX0009 — Exit Open Above Exit Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0009ExitOpenAboveExitCloseRule(SpecRule):
    rule_id = "EX0009"
    rule_name = "Exit Open Above Exit Close"


def evaluate_ex0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0009."""
    return run_spec_rule(EX0009ExitOpenAboveExitCloseRule, df)
