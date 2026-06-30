"""SR0020 — Price Crossing Below Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0020PriceCrossingBelowHorizontalResistanceRule(SpecRule):
    rule_id = "SR0020"
    rule_name = "Price Crossing Below Horizontal Resistance"


def evaluate_sr0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0020."""
    return run_spec_rule(SR0020PriceCrossingBelowHorizontalResistanceRule, df)
