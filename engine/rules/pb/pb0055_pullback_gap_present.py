"""PB0055 — Pullback Gap Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0055PullbackGapPresentRule(SpecRule):
    rule_id = "PB0055"
    rule_name = "Pullback Gap Present"


def evaluate_pb0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0055."""
    return run_spec_rule(PB0055PullbackGapPresentRule, df)
