"""PA0050 — Price Below Last Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0050PriceBelowLastSwingLowRule(SpecRule):
    rule_id = "PA0050"
    rule_name = "Price Below Last Swing Low"


def evaluate_pa0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0050."""
    return run_spec_rule(PA0050PriceBelowLastSwingLowRule, df)
