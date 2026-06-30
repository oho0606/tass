"""PB0002 — Retracement Below 38.2 Percent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0002RetracementBelow382PercentRule(SpecRule):
    rule_id = "PB0002"
    rule_name = "Retracement Below 38.2 Percent"


def evaluate_pb0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0002."""
    return run_spec_rule(PB0002RetracementBelow382PercentRule, df)
