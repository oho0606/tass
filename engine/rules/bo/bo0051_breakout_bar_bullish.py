"""BO0051 — Breakout Bar Bullish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0051BreakoutBarBullishRule(SpecRule):
    rule_id = "BO0051"
    rule_name = "Breakout Bar Bullish"


def evaluate_bo0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0051."""
    return run_spec_rule(BO0051BreakoutBarBullishRule, df)
