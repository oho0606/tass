"""PT0052 — Pattern Lower Boundary Defined. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0052PatternLowerBoundaryDefinedRule(SpecRule):
    rule_id = "PT0052"
    rule_name = "Pattern Lower Boundary Defined"


def evaluate_pt0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0052."""
    return run_spec_rule(PT0052PatternLowerBoundaryDefinedRule, df)
