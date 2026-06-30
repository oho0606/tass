"""SR0023 — Price At Dynamic Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0023PriceAtDynamicSupportRule(SpecRule):
    rule_id = "SR0023"
    rule_name = "Price At Dynamic Support"


def evaluate_sr0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0023."""
    return run_spec_rule(SR0023PriceAtDynamicSupportRule, df)
