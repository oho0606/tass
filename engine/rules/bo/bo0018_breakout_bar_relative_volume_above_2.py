"""BO0018 — Breakout Bar Relative Volume Above 2. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0018BreakoutBarRelativeVolumeAbove2Rule(SpecRule):
    rule_id = "BO0018"
    rule_name = "Breakout Bar Relative Volume Above 2"


def evaluate_bo0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0018."""
    return run_spec_rule(BO0018BreakoutBarRelativeVolumeAbove2Rule, df)
