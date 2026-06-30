"""MR0054 — ADX Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0054ADXFallingRule(SpecRule):
    rule_id = "MR0054"
    rule_name = "ADX Falling"


def evaluate_mr0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0054."""
    return run_spec_rule(MR0054ADXFallingRule, df)
