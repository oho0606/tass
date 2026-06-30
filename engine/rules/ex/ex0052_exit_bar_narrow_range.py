"""EX0052 — Exit Bar Narrow Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0052ExitBarNarrowRangeRule(SpecRule):
    rule_id = "EX0052"
    rule_name = "Exit Bar Narrow Range"


def evaluate_ex0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0052."""
    return run_spec_rule(EX0052ExitBarNarrowRangeRule, df)
