"""PB0016 — Pullback Range Wider Than Prior Leg. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0016PullbackRangeWiderThanPriorLegRule(SpecRule):
    rule_id = "PB0016"
    rule_name = "Pullback Range Wider Than Prior Leg"


def evaluate_pb0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0016."""
    return run_spec_rule(PB0016PullbackRangeWiderThanPriorLegRule, df)
