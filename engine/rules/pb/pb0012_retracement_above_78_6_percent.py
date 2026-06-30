"""PB0012 — Retracement Above 78.6 Percent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0012RetracementAbove786PercentRule(SpecRule):
    rule_id = "PB0012"
    rule_name = "Retracement Above 78.6 Percent"


def evaluate_pb0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0012."""
    return run_spec_rule(PB0012RetracementAbove786PercentRule, df)
