"""SR0040 — Price At S2. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0040PriceAtS2Rule(SpecRule):
    rule_id = "SR0040"
    rule_name = "Price At S2"


def evaluate_sr0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0040."""
    return run_spec_rule(SR0040PriceAtS2Rule, df)
