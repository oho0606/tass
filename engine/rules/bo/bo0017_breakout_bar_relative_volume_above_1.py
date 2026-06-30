"""BO0017 — Breakout Bar Relative Volume Above 1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0017BreakoutBarRelativeVolumeAbove1Rule(SpecRule):
    rule_id = "BO0017"
    rule_name = "Breakout Bar Relative Volume Above 1"


def evaluate_bo0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0017."""
    return run_spec_rule(BO0017BreakoutBarRelativeVolumeAbove1Rule, df)
