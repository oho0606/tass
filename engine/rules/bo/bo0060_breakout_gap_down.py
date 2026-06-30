"""BO0060 — Breakout Gap Down. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0060BreakoutGapDownRule(SpecRule):
    rule_id = "BO0060"
    rule_name = "Breakout Gap Down"


def evaluate_bo0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0060."""
    return run_spec_rule(BO0060BreakoutGapDownRule, df)
