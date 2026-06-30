"""BO0052 — Breakout Bar Bearish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0052BreakoutBarBearishRule(SpecRule):
    rule_id = "BO0052"
    rule_name = "Breakout Bar Bearish"


def evaluate_bo0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0052."""
    return run_spec_rule(BO0052BreakoutBarBearishRule, df)
