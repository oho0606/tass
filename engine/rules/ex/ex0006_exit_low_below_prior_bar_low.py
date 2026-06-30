"""EX0006 — Exit Low Below Prior Bar Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0006ExitLowBelowPriorBarLowRule(SpecRule):
    rule_id = "EX0006"
    rule_name = "Exit Low Below Prior Bar Low"


def evaluate_ex0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0006."""
    return run_spec_rule(EX0006ExitLowBelowPriorBarLowRule, df)
