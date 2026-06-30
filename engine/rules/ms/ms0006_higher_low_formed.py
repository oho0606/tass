"""MS0006 — Higher Low Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0006HigherLowFormedRule(SpecRule):
    rule_id = "MS0006"
    rule_name = "Higher Low Formed"


def evaluate_ms0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0006."""
    return run_spec_rule(MS0006HigherLowFormedRule, df)
