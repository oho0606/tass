"""BO0057 — Breakout Body Above Half Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0057BreakoutBodyAboveHalfRangeRule(SpecRule):
    rule_id = "BO0057"
    rule_name = "Breakout Body Above Half Range"


def evaluate_bo0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0057."""
    return run_spec_rule(BO0057BreakoutBodyAboveHalfRangeRule, df)
