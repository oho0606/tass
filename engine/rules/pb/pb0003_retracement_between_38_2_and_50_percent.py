"""PB0003 — Retracement Between 38.2 And 50 Percent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0003RetracementBetween382And50PercentRule(SpecRule):
    rule_id = "PB0003"
    rule_name = "Retracement Between 38.2 And 50 Percent"


def evaluate_pb0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0003."""
    return run_spec_rule(PB0003RetracementBetween382And50PercentRule, df)
