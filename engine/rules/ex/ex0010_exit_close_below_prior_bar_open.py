"""EX0010 — Exit Close Below Prior Bar Open. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0010ExitCloseBelowPriorBarOpenRule(SpecRule):
    rule_id = "EX0010"
    rule_name = "Exit Close Below Prior Bar Open"


def evaluate_ex0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0010."""
    return run_spec_rule(EX0010ExitCloseBelowPriorBarOpenRule, df)
