"""SR0014 — Price Near Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0014PriceNearHorizontalResistanceRule(SpecRule):
    rule_id = "SR0014"
    rule_name = "Price Near Horizontal Resistance"


def evaluate_sr0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0014."""
    return run_spec_rule(SR0014PriceNearHorizontalResistanceRule, df)
