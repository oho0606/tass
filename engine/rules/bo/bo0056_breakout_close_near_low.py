"""BO0056 — Breakout Close Near Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0056BreakoutCloseNearLowRule(SpecRule):
    rule_id = "BO0056"
    rule_name = "Breakout Close Near Low"


def evaluate_bo0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0056."""
    return run_spec_rule(BO0056BreakoutCloseNearLowRule, df)
