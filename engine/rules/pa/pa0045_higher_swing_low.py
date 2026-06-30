"""PA0045 — Higher Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0045HigherSwingLowRule(SpecRule):
    rule_id = "PA0045"
    rule_name = "Higher Swing Low"


def evaluate_pa0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0045."""
    return run_spec_rule(PA0045HigherSwingLowRule, df)
