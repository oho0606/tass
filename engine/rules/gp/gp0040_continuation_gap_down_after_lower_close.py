"""GP0040 — Continuation Gap Down After Lower Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0040ContinuationGapDownAfterLowerCloseRule(SpecRule):
    rule_id = "GP0040"
    rule_name = "Continuation Gap Down After Lower Close"


def evaluate_gp0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0040."""
    return run_spec_rule(GP0040ContinuationGapDownAfterLowerCloseRule, df)
