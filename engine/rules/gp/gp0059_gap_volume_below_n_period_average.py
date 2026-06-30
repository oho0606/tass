"""GP0059 — Gap Volume Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0059GapVolumeBelowNPeriodAverageRule(SpecRule):
    rule_id = "GP0059"
    rule_name = "Gap Volume Below N-Period Average"


def evaluate_gp0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0059."""
    return run_spec_rule(GP0059GapVolumeBelowNPeriodAverageRule, df)
