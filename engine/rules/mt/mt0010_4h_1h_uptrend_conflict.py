"""MT0010 — 4H 1H Uptrend Conflict. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT00104H1HUptrendConflictRule(SpecRule):
    rule_id = "MT0010"
    rule_name = "4H 1H Uptrend Conflict"


def evaluate_mt0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0010."""
    return run_spec_rule(MT00104H1HUptrendConflictRule, df)
