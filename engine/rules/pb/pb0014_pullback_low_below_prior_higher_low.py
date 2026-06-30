"""PB0014 — Pullback Low Below Prior Higher Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0014PullbackLowBelowPriorHigherLowRule(SpecRule):
    rule_id = "PB0014"
    rule_name = "Pullback Low Below Prior Higher Low"


def evaluate_pb0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0014."""
    return run_spec_rule(PB0014PullbackLowBelowPriorHigherLowRule, df)
