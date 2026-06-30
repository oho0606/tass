"""BO0053 — Breakout Bar Wide Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0053BreakoutBarWideRangeRule(SpecRule):
    rule_id = "BO0053"
    rule_name = "Breakout Bar Wide Range"


def evaluate_bo0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0053."""
    return run_spec_rule(BO0053BreakoutBarWideRangeRule, df)
