"""PB0010 — Pullback Bar Count Fewer Than N. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0010PullbackBarCountFewerThanNRule(SpecRule):
    rule_id = "PB0010"
    rule_name = "Pullback Bar Count Fewer Than N"


def evaluate_pb0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0010."""
    return run_spec_rule(PB0010PullbackBarCountFewerThanNRule, df)
