"""BO0058 — Breakout Body Below Half Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0058BreakoutBodyBelowHalfRangeRule(SpecRule):
    rule_id = "BO0058"
    rule_name = "Breakout Body Below Half Range"


def evaluate_bo0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0058."""
    return run_spec_rule(BO0058BreakoutBodyBelowHalfRangeRule, df)
