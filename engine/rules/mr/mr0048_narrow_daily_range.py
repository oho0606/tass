"""MR0048 — Narrow Daily Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0048NarrowDailyRangeRule(SpecRule):
    rule_id = "MR0048"
    rule_name = "Narrow Daily Range"


def evaluate_mr0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0048."""
    return run_spec_rule(MR0048NarrowDailyRangeRule, df)
