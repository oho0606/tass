"""GP0035 — Continuation Gap Up After Higher Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0035ContinuationGapUpAfterHigherCloseRule(SpecRule):
    rule_id = "GP0035"
    rule_name = "Continuation Gap Up After Higher Close"


def evaluate_gp0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0035."""
    return run_spec_rule(GP0035ContinuationGapUpAfterHigherCloseRule, df)
