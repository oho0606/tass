"""PB0020 — Pullback Bar Count Greater Than N. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0020PullbackBarCountGreaterThanNRule(SpecRule):
    rule_id = "PB0020"
    rule_name = "Pullback Bar Count Greater Than N"


def evaluate_pb0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0020."""
    return run_spec_rule(PB0020PullbackBarCountGreaterThanNRule, df)
