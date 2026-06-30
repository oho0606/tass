"""VO0036 — Price Inside Bollinger Bands. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0036PriceInsideBollingerBandsRule(SpecRule):
    rule_id = "VO0036"
    rule_name = "Price Inside Bollinger Bands"


def evaluate_vo0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0036."""
    return run_spec_rule(VO0036PriceInsideBollingerBandsRule, df)
