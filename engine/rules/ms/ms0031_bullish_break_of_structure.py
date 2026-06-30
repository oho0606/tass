"""MS0031 — Bullish Break of Structure. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0031BullishBreakofStructureRule(SpecRule):
    rule_id = "MS0031"
    rule_name = "Bullish Break of Structure"


def evaluate_ms0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0031."""
    return run_spec_rule(MS0031BullishBreakofStructureRule, df)
