"""SR0034 — Price Above S1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0034PriceAboveS1Rule(SpecRule):
    rule_id = "SR0034"
    rule_name = "Price Above S1"


def evaluate_sr0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0034."""
    return run_spec_rule(SR0034PriceAboveS1Rule, df)
