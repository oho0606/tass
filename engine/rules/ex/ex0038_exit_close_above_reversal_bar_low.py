"""EX0038 — Exit Close Above Reversal Bar Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0038ExitCloseAboveReversalBarLowRule(SpecRule):
    rule_id = "EX0038"
    rule_name = "Exit Close Above Reversal Bar Low"


def evaluate_ex0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0038."""
    return run_spec_rule(EX0038ExitCloseAboveReversalBarLowRule, df)
