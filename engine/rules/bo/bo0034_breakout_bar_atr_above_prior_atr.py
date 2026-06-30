"""BO0034 — Breakout Bar ATR Above Prior ATR. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0034BreakoutBarATRAbovePriorATRRule(SpecRule):
    rule_id = "BO0034"
    rule_name = "Breakout Bar ATR Above Prior ATR"


def evaluate_bo0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0034."""
    return run_spec_rule(BO0034BreakoutBarATRAbovePriorATRRule, df)
