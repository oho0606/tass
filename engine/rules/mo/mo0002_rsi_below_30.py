"""MO0002 — RSI Below 30. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0002RSIBelow30Rule(SpecRule):
    rule_id = "MO0002"
    rule_name = "RSI Below 30"


def evaluate_mo0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0002."""
    return run_spec_rule(MO0002RSIBelow30Rule, df)
