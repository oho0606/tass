"""PA0044 — Lower Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0044LowerSwingHighRule(SpecRule):
    rule_id = "PA0044"
    rule_name = "Lower Swing High"


def evaluate_pa0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0044."""
    return run_spec_rule(PA0044LowerSwingHighRule, df)
