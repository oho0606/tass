"""SR0009 — N-Period Low As Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0009NPeriodLowAsHorizontalSupportRule(SpecRule):
    rule_id = "SR0009"
    rule_name = "N-Period Low As Horizontal Support"


def evaluate_sr0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0009."""
    return run_spec_rule(SR0009NPeriodLowAsHorizontalSupportRule, df)
