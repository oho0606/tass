"""SR0031 — Price Above Pivot Point. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0031PriceAbovePivotPointRule(SpecRule):
    rule_id = "SR0031"
    rule_name = "Price Above Pivot Point"


def evaluate_sr0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0031."""
    return run_spec_rule(SR0031PriceAbovePivotPointRule, df)
