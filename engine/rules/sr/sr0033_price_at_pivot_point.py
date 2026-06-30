"""SR0033 — Price At Pivot Point. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0033PriceAtPivotPointRule(SpecRule):
    rule_id = "SR0033"
    rule_name = "Price At Pivot Point"


def evaluate_sr0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0033."""
    return run_spec_rule(SR0033PriceAtPivotPointRule, df)
