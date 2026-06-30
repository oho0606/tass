"""MS0038 — Bearish BOS On Current Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0038BearishBOSOnCurrentBarRule(SpecRule):
    rule_id = "MS0038"
    rule_name = "Bearish BOS On Current Bar"


def evaluate_ms0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0038."""
    return run_spec_rule(MS0038BearishBOSOnCurrentBarRule, df)
