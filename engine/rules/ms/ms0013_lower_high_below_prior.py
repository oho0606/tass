"""MS0013 — Lower High Below Prior. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0013LowerHighBelowPriorRule(SpecRule):
    rule_id = "MS0013"
    rule_name = "Lower High Below Prior"


def evaluate_ms0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0013."""
    return run_spec_rule(MS0013LowerHighBelowPriorRule, df)
