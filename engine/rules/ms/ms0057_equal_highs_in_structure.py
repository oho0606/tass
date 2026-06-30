"""MS0057 — Equal Highs In Structure. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0057EqualHighsInStructureRule(SpecRule):
    rule_id = "MS0057"
    rule_name = "Equal Highs In Structure"


def evaluate_ms0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0057."""
    return run_spec_rule(MS0057EqualHighsInStructureRule, df)
