"""VO0004 — ATR Below Prior ATR. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0004ATRBelowPriorATRRule(SpecRule):
    rule_id = "VO0004"
    rule_name = "ATR Below Prior ATR"


def evaluate_vo0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0004."""
    return run_spec_rule(VO0004ATRBelowPriorATRRule, df)
