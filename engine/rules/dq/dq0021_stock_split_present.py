"""DQ0021 — Stock Split Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0021StockSplitPresentRule(SpecRule):
    rule_id = "DQ0021"
    rule_name = "Stock Split Present"


def evaluate_dq0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0021."""
    return run_spec_rule(DQ0021StockSplitPresentRule, df)
