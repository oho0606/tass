"""SR0004 — Price Near Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0004PriceNearHorizontalSupportRule(SpecRule):
    rule_id = "SR0004"
    rule_name = "Price Near Horizontal Support"


def evaluate_sr0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0004."""
    return run_spec_rule(SR0004PriceNearHorizontalSupportRule, df)
