"""BO0059 — Breakout Gap Up. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0059BreakoutGapUpRule(SpecRule):
    rule_id = "BO0059"
    rule_name = "Breakout Gap Up"


def evaluate_bo0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0059."""
    return run_spec_rule(BO0059BreakoutGapUpRule, df)
