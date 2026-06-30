"""BO0048 — Close Below Trendline Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0048CloseBelowTrendlineSupportRule(SpecRule):
    rule_id = "BO0048"
    rule_name = "Close Below Trendline Support"


def evaluate_bo0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0048."""
    return run_spec_rule(BO0048CloseBelowTrendlineSupportRule, df)
