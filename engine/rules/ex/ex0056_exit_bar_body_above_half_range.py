"""EX0056 — Exit Bar Body Above Half Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0056ExitBarBodyAboveHalfRangeRule(SpecRule):
    rule_id = "EX0056"
    rule_name = "Exit Bar Body Above Half Range"


def evaluate_ex0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0056."""
    return run_spec_rule(EX0056ExitBarBodyAboveHalfRangeRule, df)
