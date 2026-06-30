"""BO0003 — High Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0003HighAboveNPeriodHighRule(SpecRule):
    rule_id = "BO0003"
    rule_name = "High Above N-Period High"


def evaluate_bo0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0003."""
    return run_spec_rule(BO0003HighAboveNPeriodHighRule, df)
