"""PB0056 — Pullback Close Near Bar High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0056PullbackCloseNearBarHighRule(SpecRule):
    rule_id = "PB0056"
    rule_name = "Pullback Close Near Bar High"


def evaluate_pb0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0056."""
    return run_spec_rule(PB0056PullbackCloseNearBarHighRule, df)
