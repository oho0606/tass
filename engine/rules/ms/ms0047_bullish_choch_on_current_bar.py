"""MS0047 — Bullish CHoCH On Current Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0047BullishCHoCHOnCurrentBarRule(SpecRule):
    rule_id = "MS0047"
    rule_name = "Bullish CHoCH On Current Bar"


def evaluate_ms0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0047."""
    return run_spec_rule(MS0047BullishCHoCHOnCurrentBarRule, df)
