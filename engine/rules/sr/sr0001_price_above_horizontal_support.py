"""SR0001 — Price Above Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0001PriceAboveHorizontalSupportRule(SpecRule):
    rule_id = "SR0001"
    rule_name = "Price Above Horizontal Support"


def evaluate_sr0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0001."""
    return run_spec_rule(SR0001PriceAboveHorizontalSupportRule, df)
