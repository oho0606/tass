"""MS0029 — Equal Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0029EqualSwingHighRule(SpecRule):
    rule_id = "MS0029"
    rule_name = "Equal Swing High"


def evaluate_ms0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0029."""
    return run_spec_rule(MS0029EqualSwingHighRule, df)
