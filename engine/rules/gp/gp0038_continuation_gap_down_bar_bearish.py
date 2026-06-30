"""GP0038 — Continuation Gap Down Bar Bearish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0038ContinuationGapDownBarBearishRule(SpecRule):
    rule_id = "GP0038"
    rule_name = "Continuation Gap Down Bar Bearish"


def evaluate_gp0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0038."""
    return run_spec_rule(GP0038ContinuationGapDownBarBearishRule, df)
