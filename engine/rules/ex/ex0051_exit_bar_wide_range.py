"""EX0051 — Exit Bar Wide Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0051ExitBarWideRangeRule(SpecRule):
    rule_id = "EX0051"
    rule_name = "Exit Bar Wide Range"


def evaluate_ex0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0051."""
    return run_spec_rule(EX0051ExitBarWideRangeRule, df)
