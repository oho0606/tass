"""MS0011 — Lower High Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0011LowerHighFormedRule(SpecRule):
    rule_id = "MS0011"
    rule_name = "Lower High Formed"


def evaluate_ms0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0011."""
    return run_spec_rule(MS0011LowerHighFormedRule, df)
