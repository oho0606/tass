"""MR0040 — Consecutive Wide Range Bars. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0040ConsecutiveWideRangeBarsRule(SpecRule):
    rule_id = "MR0040"
    rule_name = "Consecutive Wide Range Bars"


def evaluate_mr0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0040."""
    return run_spec_rule(MR0040ConsecutiveWideRangeBarsRule, df)
