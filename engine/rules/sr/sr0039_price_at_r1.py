"""SR0039 — Price At R1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0039PriceAtR1Rule(SpecRule):
    rule_id = "SR0039"
    rule_name = "Price At R1"


def evaluate_sr0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0039."""
    return run_spec_rule(SR0039PriceAtR1Rule, df)
