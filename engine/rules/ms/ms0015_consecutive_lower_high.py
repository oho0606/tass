"""MS0015 — Consecutive Lower High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0015ConsecutiveLowerHighRule(SpecRule):
    rule_id = "MS0015"
    rule_name = "Consecutive Lower High"


def evaluate_ms0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0015."""
    return run_spec_rule(MS0015ConsecutiveLowerHighRule, df)
