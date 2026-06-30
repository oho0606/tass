"""BO0038 — Breakout Bar Volatility Expanding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0038BreakoutBarVolatilityExpandingRule(SpecRule):
    rule_id = "BO0038"
    rule_name = "Breakout Bar Volatility Expanding"


def evaluate_bo0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0038."""
    return run_spec_rule(BO0038BreakoutBarVolatilityExpandingRule, df)
