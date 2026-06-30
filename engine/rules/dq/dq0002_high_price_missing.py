"""DQ0002 — High Price Missing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0002HighPriceMissingRule(SpecRule):
    rule_id = "DQ0002"
    rule_name = "High Price Missing"


def evaluate_dq0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0002."""
    return run_spec_rule(DQ0002HighPriceMissingRule, df)
