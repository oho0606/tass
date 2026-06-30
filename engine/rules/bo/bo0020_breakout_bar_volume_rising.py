"""BO0020 — Breakout Bar Volume Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0020BreakoutBarVolumeRisingRule(SpecRule):
    rule_id = "BO0020"
    rule_name = "Breakout Bar Volume Rising"


def evaluate_bo0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0020."""
    return run_spec_rule(BO0020BreakoutBarVolumeRisingRule, df)
