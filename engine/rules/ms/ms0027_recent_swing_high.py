"""MS0027 — Recent Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0027RecentSwingHighRule(SpecRule):
    rule_id = "MS0027"
    rule_name = "Recent Swing High"


def evaluate_ms0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0027."""
    return run_spec_rule(MS0027RecentSwingHighRule, df)
