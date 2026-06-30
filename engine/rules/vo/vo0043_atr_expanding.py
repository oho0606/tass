"""VO0043 — ATR Expanding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0043ATRExpandingRule(SpecRule):
    rule_id = "VO0043"
    rule_name = "ATR Expanding"


def evaluate_vo0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0043."""
    return run_spec_rule(VO0043ATRExpandingRule, df)
