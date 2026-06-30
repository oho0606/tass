"""GP0032 — Continuation Gap Up Unfilled At Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0032ContinuationGapUpUnfilledAtCloseRule(SpecRule):
    rule_id = "GP0032"
    rule_name = "Continuation Gap Up Unfilled At Close"


def evaluate_gp0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0032."""
    return run_spec_rule(GP0032ContinuationGapUpUnfilledAtCloseRule, df)
