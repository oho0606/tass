"""GP0036 — Continuation Gap Down High Below Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0036ContinuationGapDownHighBelowPriorLowRule(SpecRule):
    rule_id = "GP0036"
    rule_name = "Continuation Gap Down High Below Prior Low"


def evaluate_gp0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0036."""
    return run_spec_rule(GP0036ContinuationGapDownHighBelowPriorLowRule, df)
