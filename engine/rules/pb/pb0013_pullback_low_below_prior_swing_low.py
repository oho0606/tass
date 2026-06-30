"""PB0013 — Pullback Low Below Prior Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0013PullbackLowBelowPriorSwingLowRule(SpecRule):
    rule_id = "PB0013"
    rule_name = "Pullback Low Below Prior Swing Low"


def evaluate_pb0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0013."""
    return run_spec_rule(PB0013PullbackLowBelowPriorSwingLowRule, df)
