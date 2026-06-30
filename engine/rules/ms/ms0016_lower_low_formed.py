"""MS0016 — Lower Low Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0016LowerLowFormedRule(SpecRule):
    rule_id = "MS0016"
    rule_name = "Lower Low Formed"


def evaluate_ms0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0016."""
    return run_spec_rule(MS0016LowerLowFormedRule, df)
