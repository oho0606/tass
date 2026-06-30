"""PT0051 — Pattern Upper Boundary Defined. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0051PatternUpperBoundaryDefinedRule(SpecRule):
    rule_id = "PT0051"
    rule_name = "Pattern Upper Boundary Defined"


def evaluate_pt0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0051."""
    return run_spec_rule(PT0051PatternUpperBoundaryDefinedRule, df)
