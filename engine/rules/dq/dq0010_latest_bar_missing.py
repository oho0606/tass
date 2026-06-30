"""DQ0010 — Latest Bar Missing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0010LatestBarMissingRule(SpecRule):
    rule_id = "DQ0010"
    rule_name = "Latest Bar Missing"


def evaluate_dq0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0010."""
    return run_spec_rule(DQ0010LatestBarMissingRule, df)
