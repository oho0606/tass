"""VO0010 — ATR Turning. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0010ATRTurningRule(SpecRule):
    rule_id = "VO0010"
    rule_name = "ATR Turning"


def evaluate_vo0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0010."""
    return run_spec_rule(VO0010ATRTurningRule, df)
