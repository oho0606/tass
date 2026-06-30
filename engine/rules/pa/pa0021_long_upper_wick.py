"""PA0021 — Long Upper Wick. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0021LongUpperWickRule(SpecRule):
    rule_id = "PA0021"
    rule_name = "Long Upper Wick"


def evaluate_pa0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0021."""
    return run_spec_rule(PA0021LongUpperWickRule, df)
