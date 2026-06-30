"""PB0008 — Pullback Range Narrower Than Prior Leg. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0008PullbackRangeNarrowerThanPriorLegRule(SpecRule):
    rule_id = "PB0008"
    rule_name = "Pullback Range Narrower Than Prior Leg"


def evaluate_pb0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0008."""
    return run_spec_rule(PB0008PullbackRangeNarrowerThanPriorLegRule, df)
