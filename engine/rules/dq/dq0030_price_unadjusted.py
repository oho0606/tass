"""DQ0030 — Price Unadjusted. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0030PriceUnadjustedRule(SpecRule):
    rule_id = "DQ0030"
    rule_name = "Price Unadjusted"


def evaluate_dq0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0030."""
    return run_spec_rule(DQ0030PriceUnadjustedRule, df)
