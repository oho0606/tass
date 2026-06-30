"""MS0028 — Recent Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0028RecentSwingLowRule(SpecRule):
    rule_id = "MS0028"
    rule_name = "Recent Swing Low"


def evaluate_ms0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0028."""
    return run_spec_rule(MS0028RecentSwingLowRule, df)
