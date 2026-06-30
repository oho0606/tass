"""MS0044 — CHoCH Below Higher Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0044CHoCHBelowHigherLowRule(SpecRule):
    rule_id = "MS0044"
    rule_name = "CHoCH Below Higher Low"


def evaluate_ms0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0044."""
    return run_spec_rule(MS0044CHoCHBelowHigherLowRule, df)
