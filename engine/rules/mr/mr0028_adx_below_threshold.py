"""MR0028 — ADX Below Threshold. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0028ADXBelowThresholdRule(SpecRule):
    rule_id = "MR0028"
    rule_name = "ADX Below Threshold"


def evaluate_mr0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0028."""
    return run_spec_rule(MR0028ADXBelowThresholdRule, df)
