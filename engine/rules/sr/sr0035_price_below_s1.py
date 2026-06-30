"""SR0035 — Price Below S1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0035PriceBelowS1Rule(SpecRule):
    rule_id = "SR0035"
    rule_name = "Price Below S1"


def evaluate_sr0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0035."""
    return run_spec_rule(SR0035PriceBelowS1Rule, df)
