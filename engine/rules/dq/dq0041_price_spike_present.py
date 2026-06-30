"""DQ0041 — Price Spike Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0041PriceSpikePresentRule(SpecRule):
    rule_id = "DQ0041"
    rule_name = "Price Spike Present"


def evaluate_dq0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0041."""
    return run_spec_rule(DQ0041PriceSpikePresentRule, df)
