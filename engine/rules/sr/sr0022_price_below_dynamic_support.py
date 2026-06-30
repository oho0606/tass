"""SR0022 — Price Below Dynamic Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0022PriceBelowDynamicSupportRule(SpecRule):
    rule_id = "SR0022"
    rule_name = "Price Below Dynamic Support"


def evaluate_sr0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0022."""
    return run_spec_rule(SR0022PriceBelowDynamicSupportRule, df)
