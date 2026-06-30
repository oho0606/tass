"""VO0002 — ATR Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0002ATRFallingRule(SpecRule):
    rule_id = "VO0002"
    rule_name = "ATR Falling"


def evaluate_vo0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0002."""
    return run_spec_rule(VO0002ATRFallingRule, df)
