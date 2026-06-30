"""DQ0057 — Data Feed Current. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0057DataFeedCurrentRule(SpecRule):
    rule_id = "DQ0057"
    rule_name = "Data Feed Current"


def evaluate_dq0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0057."""
    return run_spec_rule(DQ0057DataFeedCurrentRule, df)
