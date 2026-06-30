"""BO0054 — Breakout Bar Narrow Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0054BreakoutBarNarrowRangeRule(SpecRule):
    rule_id = "BO0054"
    rule_name = "Breakout Bar Narrow Range"


def evaluate_bo0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0054."""
    return run_spec_rule(BO0054BreakoutBarNarrowRangeRule, df)
