"""SR0038 — Price Below R1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0038PriceBelowR1Rule(SpecRule):
    rule_id = "SR0038"
    rule_name = "Price Below R1"


def evaluate_sr0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0038."""
    return run_spec_rule(SR0038PriceBelowR1Rule, df)
