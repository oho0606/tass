"""PT0015 — Rounding Top Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0015RoundingTopFormedRule(SpecRule):
    rule_id = "PT0015"
    rule_name = "Rounding Top Formed"


def evaluate_pt0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0015."""
    return run_spec_rule(PT0015RoundingTopFormedRule, df)
