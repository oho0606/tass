"""VO0016 — True Range At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0016TrueRangeAtNPeriodLowRule(SpecRule):
    rule_id = "VO0016"
    rule_name = "True Range At N-Period Low"


def evaluate_vo0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0016."""
    return run_spec_rule(VO0016TrueRangeAtNPeriodLowRule, df)
