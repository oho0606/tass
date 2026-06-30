"""PB0057 — Pullback Close Near Bar Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0057PullbackCloseNearBarLowRule(SpecRule):
    rule_id = "PB0057"
    rule_name = "Pullback Close Near Bar Low"


def evaluate_pb0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0057."""
    return run_spec_rule(PB0057PullbackCloseNearBarLowRule, df)
