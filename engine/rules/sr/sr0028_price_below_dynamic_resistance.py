"""SR0028 — Price Below Dynamic Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0028PriceBelowDynamicResistanceRule(SpecRule):
    rule_id = "SR0028"
    rule_name = "Price Below Dynamic Resistance"


def evaluate_sr0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0028."""
    return run_spec_rule(SR0028PriceBelowDynamicResistanceRule, df)
