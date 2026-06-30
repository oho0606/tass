"""SR0010 — Price Crossing Above Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0010PriceCrossingAboveHorizontalSupportRule(SpecRule):
    rule_id = "SR0010"
    rule_name = "Price Crossing Above Horizontal Support"


def evaluate_sr0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0010."""
    return run_spec_rule(SR0010PriceCrossingAboveHorizontalSupportRule, df)
