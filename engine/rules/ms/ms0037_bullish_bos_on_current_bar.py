"""MS0037 — Bullish BOS On Current Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0037BullishBOSOnCurrentBarRule(SpecRule):
    rule_id = "MS0037"
    rule_name = "Bullish BOS On Current Bar"


def evaluate_ms0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0037."""
    return run_spec_rule(MS0037BullishBOSOnCurrentBarRule, df)
