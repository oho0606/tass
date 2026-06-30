"""VO0058 — Consecutive Stable ATR. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0058ConsecutiveStableATRRule(SpecRule):
    rule_id = "VO0058"
    rule_name = "Consecutive Stable ATR"


def evaluate_vo0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0058."""
    return run_spec_rule(VO0058ConsecutiveStableATRRule, df)
