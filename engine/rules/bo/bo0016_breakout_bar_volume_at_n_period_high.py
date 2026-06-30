"""BO0016 — Breakout Bar Volume At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0016BreakoutBarVolumeAtNPeriodHighRule(SpecRule):
    rule_id = "BO0016"
    rule_name = "Breakout Bar Volume At N-Period High"


def evaluate_bo0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0016."""
    return run_spec_rule(BO0016BreakoutBarVolumeAtNPeriodHighRule, df)
