"""BO0005 — Open Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0005OpenAboveNPeriodHighRule(SpecRule):
    rule_id = "BO0005"
    rule_name = "Open Above N-Period High"


def evaluate_bo0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0005."""
    return run_spec_rule(BO0005OpenAboveNPeriodHighRule, df)
