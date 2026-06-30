"""PB0054 — Pullback Range Expanding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0054PullbackRangeExpandingRule(SpecRule):
    rule_id = "PB0054"
    rule_name = "Pullback Range Expanding"


def evaluate_pb0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0054."""
    return run_spec_rule(PB0054PullbackRangeExpandingRule, df)
