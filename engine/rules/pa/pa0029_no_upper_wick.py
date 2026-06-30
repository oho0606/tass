"""PA0029 — No Upper Wick. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0029NoUpperWickRule(SpecRule):
    rule_id = "PA0029"
    rule_name = "No Upper Wick"


def evaluate_pa0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0029."""
    return run_spec_rule(PA0029NoUpperWickRule, df)
