"""VO0007 — ATR At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0007ATRAtNPeriodHighRule(SpecRule):
    rule_id = "VO0007"
    rule_name = "ATR At N-Period High"


def evaluate_vo0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0007."""
    return run_spec_rule(VO0007ATRAtNPeriodHighRule, df)
