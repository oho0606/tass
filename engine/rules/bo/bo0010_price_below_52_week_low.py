"""BO0010 — Price Below 52-Week Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0010PriceBelow52WeekLowRule(SpecRule):
    rule_id = "BO0010"
    rule_name = "Price Below 52-Week Low"


def evaluate_bo0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0010."""
    return run_spec_rule(BO0010PriceBelow52WeekLowRule, df)
