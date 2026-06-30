"""PB0004 — Retracement Between 50 And 61.8 Percent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0004RetracementBetween50And618PercentRule(SpecRule):
    rule_id = "PB0004"
    rule_name = "Retracement Between 50 And 61.8 Percent"


def evaluate_pb0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0004."""
    return run_spec_rule(PB0004RetracementBetween50And618PercentRule, df)
