"""PB0006 — Pullback High Below Prior Swing High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0006PullbackHighBelowPriorSwingHighRule(SpecRule):
    rule_id = "PB0006"
    rule_name = "Pullback High Below Prior Swing High"


def evaluate_pb0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0006."""
    return run_spec_rule(PB0006PullbackHighBelowPriorSwingHighRule, df)
