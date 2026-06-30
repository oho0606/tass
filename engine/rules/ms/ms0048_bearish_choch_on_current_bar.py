"""MS0048 — Bearish CHoCH On Current Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0048BearishCHoCHOnCurrentBarRule(SpecRule):
    rule_id = "MS0048"
    rule_name = "Bearish CHoCH On Current Bar"


def evaluate_ms0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0048."""
    return run_spec_rule(MS0048BearishCHoCHOnCurrentBarRule, df)
