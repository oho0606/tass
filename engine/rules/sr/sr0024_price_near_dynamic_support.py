"""SR0024 — Price Near Dynamic Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0024PriceNearDynamicSupportRule(SpecRule):
    rule_id = "SR0024"
    rule_name = "Price Near Dynamic Support"


def evaluate_sr0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0024."""
    return run_spec_rule(SR0024PriceNearDynamicSupportRule, df)
