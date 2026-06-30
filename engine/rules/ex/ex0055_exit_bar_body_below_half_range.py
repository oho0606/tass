"""EX0055 — Exit Bar Body Below Half Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0055ExitBarBodyBelowHalfRangeRule(SpecRule):
    rule_id = "EX0055"
    rule_name = "Exit Bar Body Below Half Range"


def evaluate_ex0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0055."""
    return run_spec_rule(EX0055ExitBarBodyBelowHalfRangeRule, df)
