"""MR0019 — N-Period Return Negative. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0019NPeriodReturnNegativeRule(SpecRule):
    rule_id = "MR0019"
    rule_name = "N-Period Return Negative"


def evaluate_mr0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0019."""
    return run_spec_rule(MR0019NPeriodReturnNegativeRule, df)
