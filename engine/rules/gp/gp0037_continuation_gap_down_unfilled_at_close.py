"""GP0037 — Continuation Gap Down Unfilled At Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0037ContinuationGapDownUnfilledAtCloseRule(SpecRule):
    rule_id = "GP0037"
    rule_name = "Continuation Gap Down Unfilled At Close"


def evaluate_gp0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0037."""
    return run_spec_rule(GP0037ContinuationGapDownUnfilledAtCloseRule, df)
