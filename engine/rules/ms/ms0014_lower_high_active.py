"""MS0014 — Lower High Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0014LowerHighActiveRule(SpecRule):
    rule_id = "MS0014"
    rule_name = "Lower High Active"


def evaluate_ms0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0014."""
    return run_spec_rule(MS0014LowerHighActiveRule, df)
