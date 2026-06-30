"""DQ0020 — Price Adjustment Mismatch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0020PriceAdjustmentMismatchRule(SpecRule):
    rule_id = "DQ0020"
    rule_name = "Price Adjustment Mismatch"


def evaluate_dq0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0020."""
    return run_spec_rule(DQ0020PriceAdjustmentMismatchRule, df)
