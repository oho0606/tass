"""GP0031 — Continuation Gap Up Low Above Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0031ContinuationGapUpLowAbovePriorHighRule(SpecRule):
    rule_id = "GP0031"
    rule_name = "Continuation Gap Up Low Above Prior High"


def evaluate_gp0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0031."""
    return run_spec_rule(GP0031ContinuationGapUpLowAbovePriorHighRule, df)
