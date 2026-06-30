"""EX0001 — Exit Close Below SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0001ExitCloseBelowSMA20Rule(SpecRule):
    rule_id = "EX0001"
    rule_name = "Exit Close Below SMA20"


def evaluate_ex0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0001."""
    return run_spec_rule(EX0001ExitCloseBelowSMA20Rule, df)
