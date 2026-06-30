"""EX0037 — Exit Close Below Reversal Bar High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0037ExitCloseBelowReversalBarHighRule(SpecRule):
    rule_id = "EX0037"
    rule_name = "Exit Close Below Reversal Bar High"


def evaluate_ex0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0037."""
    return run_spec_rule(EX0037ExitCloseBelowReversalBarHighRule, df)
