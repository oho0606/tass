"""EX0048 — Exit Bar Bullish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0048ExitBarBullishRule(SpecRule):
    rule_id = "EX0048"
    rule_name = "Exit Bar Bullish"


def evaluate_ex0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0048."""
    return run_spec_rule(EX0048ExitBarBullishRule, df)
