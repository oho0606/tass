"""SR0013 — Price At Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0013PriceAtHorizontalResistanceRule(SpecRule):
    rule_id = "SR0013"
    rule_name = "Price At Horizontal Resistance"


def evaluate_sr0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0013."""
    return run_spec_rule(SR0013PriceAtHorizontalResistanceRule, df)
