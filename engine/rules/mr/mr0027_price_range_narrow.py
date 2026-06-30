"""MR0027 — Price Range Narrow. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0027PriceRangeNarrowRule(SpecRule):
    rule_id = "MR0027"
    rule_name = "Price Range Narrow"


def evaluate_mr0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0027."""
    return run_spec_rule(MR0027PriceRangeNarrowRule, df)
