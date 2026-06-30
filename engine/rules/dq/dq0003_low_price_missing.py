"""DQ0003 — Low Price Missing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0003LowPriceMissingRule(SpecRule):
    rule_id = "DQ0003"
    rule_name = "Low Price Missing"


def evaluate_dq0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0003."""
    return run_spec_rule(DQ0003LowPriceMissingRule, df)
