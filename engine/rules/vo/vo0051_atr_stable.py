"""VO0051 — ATR Stable. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0051ATRStableRule(SpecRule):
    rule_id = "VO0051"
    rule_name = "ATR Stable"


def evaluate_vo0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0051."""
    return run_spec_rule(VO0051ATRStableRule, df)
