"""PA0023 — Short Upper Wick. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0023ShortUpperWickRule(SpecRule):
    rule_id = "PA0023"
    rule_name = "Short Upper Wick"


def evaluate_pa0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0023."""
    return run_spec_rule(PA0023ShortUpperWickRule, df)
