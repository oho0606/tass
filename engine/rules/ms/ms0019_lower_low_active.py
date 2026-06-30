"""MS0019 — Lower Low Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0019LowerLowActiveRule(SpecRule):
    rule_id = "MS0019"
    rule_name = "Lower Low Active"


def evaluate_ms0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0019."""
    return run_spec_rule(MS0019LowerLowActiveRule, df)
