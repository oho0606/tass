"""SR0005 — Price Touching Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0005PriceTouchingHorizontalSupportRule(SpecRule):
    rule_id = "SR0005"
    rule_name = "Price Touching Horizontal Support"


def evaluate_sr0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0005."""
    return run_spec_rule(SR0005PriceTouchingHorizontalSupportRule, df)
