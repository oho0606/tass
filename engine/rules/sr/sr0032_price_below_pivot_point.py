"""SR0032 — Price Below Pivot Point. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0032PriceBelowPivotPointRule(SpecRule):
    rule_id = "SR0032"
    rule_name = "Price Below Pivot Point"


def evaluate_sr0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0032."""
    return run_spec_rule(SR0032PriceBelowPivotPointRule, df)
