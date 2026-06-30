"""MR0051 — ADX Above Threshold. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0051ADXAboveThresholdRule(SpecRule):
    rule_id = "MR0051"
    rule_name = "ADX Above Threshold"


def evaluate_mr0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0051."""
    return run_spec_rule(MR0051ADXAboveThresholdRule, df)
