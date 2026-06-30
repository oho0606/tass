"""PB0035 — Pullback Volume Below Prior Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0035PullbackVolumeBelowPriorBarRule(SpecRule):
    rule_id = "PB0035"
    rule_name = "Pullback Volume Below Prior Bar"


def evaluate_pb0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0035."""
    return run_spec_rule(PB0035PullbackVolumeBelowPriorBarRule, df)
