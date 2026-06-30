"""BO0055 — Breakout Close Near High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0055BreakoutCloseNearHighRule(SpecRule):
    rule_id = "BO0055"
    rule_name = "Breakout Close Near High"


def evaluate_bo0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0055."""
    return run_spec_rule(BO0055BreakoutCloseNearHighRule, df)
