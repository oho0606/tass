"""PA0031 — Wide Range Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0031WideRangeBarRule(SpecRule):
    rule_id = "PA0031"
    rule_name = "Wide Range Bar"


def evaluate_pa0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0031."""
    return run_spec_rule(PA0031WideRangeBarRule, df)
