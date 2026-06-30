"""MS0030 — Equal Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0030EqualSwingLowRule(SpecRule):
    rule_id = "MS0030"
    rule_name = "Equal Swing Low"


def evaluate_ms0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0030."""
    return run_spec_rule(MS0030EqualSwingLowRule, df)
