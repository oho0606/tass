"""PB0045 — Higher Low Formed During Pullback. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0045HigherLowFormedDuringPullbackRule(SpecRule):
    rule_id = "PB0045"
    rule_name = "Higher Low Formed During Pullback"


def evaluate_pb0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0045."""
    return run_spec_rule(PB0045HigherLowFormedDuringPullbackRule, df)
