"""PA0046 — Lower Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0046LowerSwingLowRule(SpecRule):
    rule_id = "PA0046"
    rule_name = "Lower Swing Low"


def evaluate_pa0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0046."""
    return run_spec_rule(PA0046LowerSwingLowRule, df)
