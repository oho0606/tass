"""MT0042 — Weekly Daily 4H Trend Conflict. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0042WeeklyDaily4HTrendConflictRule(SpecRule):
    rule_id = "MT0042"
    rule_name = "Weekly Daily 4H Trend Conflict"


def evaluate_mt0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0042."""
    return run_spec_rule(MT0042WeeklyDaily4HTrendConflictRule, df)
