"""EX0005 — Exit High Below Prior Bar High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0005ExitHighBelowPriorBarHighRule(SpecRule):
    rule_id = "EX0005"
    rule_name = "Exit High Below Prior Bar High"


def evaluate_ex0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0005."""
    return run_spec_rule(EX0005ExitHighBelowPriorBarHighRule, df)
