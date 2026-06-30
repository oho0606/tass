"""MR0050 — Consecutive Narrow Range Bars. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0050ConsecutiveNarrowRangeBarsRule(SpecRule):
    rule_id = "MR0050"
    rule_name = "Consecutive Narrow Range Bars"


def evaluate_mr0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0050."""
    return run_spec_rule(MR0050ConsecutiveNarrowRangeBarsRule, df)
