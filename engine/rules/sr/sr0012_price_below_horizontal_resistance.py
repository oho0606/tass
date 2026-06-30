"""SR0012 — Price Below Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0012PriceBelowHorizontalResistanceRule(SpecRule):
    rule_id = "SR0012"
    rule_name = "Price Below Horizontal Resistance"


def evaluate_sr0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0012."""
    return run_spec_rule(SR0012PriceBelowHorizontalResistanceRule, df)
