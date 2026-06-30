"""MR0038 — Wide Daily Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0038WideDailyRangeRule(SpecRule):
    rule_id = "MR0038"
    rule_name = "Wide Daily Range"


def evaluate_mr0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0038."""
    return run_spec_rule(MR0038WideDailyRangeRule, df)
