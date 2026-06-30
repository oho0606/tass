"""SR0025 — Price Touching Dynamic Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0025PriceTouchingDynamicSupportRule(SpecRule):
    rule_id = "SR0025"
    rule_name = "Price Touching Dynamic Support"


def evaluate_sr0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0025."""
    return run_spec_rule(SR0025PriceTouchingDynamicSupportRule, df)
