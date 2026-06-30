"""SR0002 — Price Below Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0002PriceBelowHorizontalSupportRule(SpecRule):
    rule_id = "SR0002"
    rule_name = "Price Below Horizontal Support"


def evaluate_sr0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0002."""
    return run_spec_rule(SR0002PriceBelowHorizontalSupportRule, df)
