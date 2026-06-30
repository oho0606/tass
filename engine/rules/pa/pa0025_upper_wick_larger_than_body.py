"""PA0025 — Upper Wick Larger Than Body. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0025UpperWickLargerThanBodyRule(SpecRule):
    rule_id = "PA0025"
    rule_name = "Upper Wick Larger Than Body"


def evaluate_pa0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0025."""
    return run_spec_rule(PA0025UpperWickLargerThanBodyRule, df)
