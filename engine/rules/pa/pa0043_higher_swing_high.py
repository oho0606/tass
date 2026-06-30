"""PA0043 — Higher Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0043HigherSwingHighRule(SpecRule):
    rule_id = "PA0043"
    rule_name = "Higher Swing High"


def evaluate_pa0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0043."""
    return run_spec_rule(PA0043HigherSwingHighRule, df)
