"""EX0002 — Exit Close Below SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0002ExitCloseBelowSMA60Rule(SpecRule):
    rule_id = "EX0002"
    rule_name = "Exit Close Below SMA60"


def evaluate_ex0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0002."""
    return run_spec_rule(EX0002ExitCloseBelowSMA60Rule, df)
