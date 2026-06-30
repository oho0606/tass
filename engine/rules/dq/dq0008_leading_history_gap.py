"""DQ0008 — Leading History Gap. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0008LeadingHistoryGapRule(SpecRule):
    rule_id = "DQ0008"
    rule_name = "Leading History Gap"


def evaluate_dq0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0008."""
    return run_spec_rule(DQ0008LeadingHistoryGapRule, df)
