"""SR0021 — Price Above Dynamic Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0021PriceAboveDynamicSupportRule(SpecRule):
    rule_id = "SR0021"
    rule_name = "Price Above Dynamic Support"


def evaluate_sr0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0021."""
    return run_spec_rule(SR0021PriceAboveDynamicSupportRule, df)
