"""SR0036 — Price At S1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0036PriceAtS1Rule(SpecRule):
    rule_id = "SR0036"
    rule_name = "Price At S1"


def evaluate_sr0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0036."""
    return run_spec_rule(SR0036PriceAtS1Rule, df)
