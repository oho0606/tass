"""DQ0001 — Open Price Missing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0001OpenPriceMissingRule(SpecRule):
    rule_id = "DQ0001"
    rule_name = "Open Price Missing"


def evaluate_dq0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0001."""
    return run_spec_rule(DQ0001OpenPriceMissingRule, df)
