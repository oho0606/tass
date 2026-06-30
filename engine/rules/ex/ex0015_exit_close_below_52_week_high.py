"""EX0015 — Exit Close Below 52-Week High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0015ExitCloseBelow52WeekHighRule(SpecRule):
    rule_id = "EX0015"
    rule_name = "Exit Close Below 52-Week High"


def evaluate_ex0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0015."""
    return run_spec_rule(EX0015ExitCloseBelow52WeekHighRule, df)
