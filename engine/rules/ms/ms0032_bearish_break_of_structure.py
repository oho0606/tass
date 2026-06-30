"""MS0032 — Bearish Break of Structure. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0032BearishBreakofStructureRule(SpecRule):
    rule_id = "MS0032"
    rule_name = "Bearish Break of Structure"


def evaluate_ms0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0032."""
    return run_spec_rule(MS0032BearishBreakofStructureRule, df)
