"""CS0045 — Four Price Doji Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0045FourPriceDojiFormedRule(SpecRule):
    rule_id = "CS0045"
    rule_name = "Four Price Doji Formed"


def evaluate_cs0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0045."""
    return run_spec_rule(CS0045FourPriceDojiFormedRule, df)
