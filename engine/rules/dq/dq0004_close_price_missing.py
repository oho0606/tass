"""DQ0004 — Close Price Missing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0004ClosePriceMissingRule(SpecRule):
    rule_id = "DQ0004"
    rule_name = "Close Price Missing"


def evaluate_dq0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0004."""
    return run_spec_rule(DQ0004ClosePriceMissingRule, df)
