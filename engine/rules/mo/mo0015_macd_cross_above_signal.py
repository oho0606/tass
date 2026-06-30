"""MO0015 — MACD Cross Above Signal. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0015MACDCrossAboveSignalRule(SpecRule):
    rule_id = "MO0015"
    rule_name = "MACD Cross Above Signal"


def evaluate_mo0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0015."""
    return run_spec_rule(MO0015MACDCrossAboveSignalRule, df)
