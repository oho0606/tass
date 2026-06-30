"""CS0038 — Bearish Side By Side White Lines Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0038BearishSideBySideWhiteLinesFormedRule(SpecRule):
    rule_id = "CS0038"
    rule_name = "Bearish Side By Side White Lines Formed"


def evaluate_cs0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0038."""
    return run_spec_rule(CS0038BearishSideBySideWhiteLinesFormedRule, df)
