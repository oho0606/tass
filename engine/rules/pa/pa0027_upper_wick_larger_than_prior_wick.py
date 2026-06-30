"""PA0027 — Upper Wick Larger Than Prior Wick. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0027UpperWickLargerThanPriorWickRule(SpecRule):
    rule_id = "PA0027"
    rule_name = "Upper Wick Larger Than Prior Wick"


def evaluate_pa0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0027."""
    return run_spec_rule(PA0027UpperWickLargerThanPriorWickRule, df)
