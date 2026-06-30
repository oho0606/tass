"""MS0058 — Equal Lows In Structure. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0058EqualLowsInStructureRule(SpecRule):
    rule_id = "MS0058"
    rule_name = "Equal Lows In Structure"


def evaluate_ms0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0058."""
    return run_spec_rule(MS0058EqualLowsInStructureRule, df)
