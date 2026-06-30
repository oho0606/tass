"""DQ0009 — Internal History Gap. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0009InternalHistoryGapRule(SpecRule):
    rule_id = "DQ0009"
    rule_name = "Internal History Gap"


def evaluate_dq0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0009."""
    return run_spec_rule(DQ0009InternalHistoryGapRule, df)
