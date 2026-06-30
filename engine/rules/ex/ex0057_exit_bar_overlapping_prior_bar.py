"""EX0057 — Exit Bar Overlapping Prior Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0057ExitBarOverlappingPriorBarRule(SpecRule):
    rule_id = "EX0057"
    rule_name = "Exit Bar Overlapping Prior Bar"


def evaluate_ex0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0057."""
    return run_spec_rule(EX0057ExitBarOverlappingPriorBarRule, df)
