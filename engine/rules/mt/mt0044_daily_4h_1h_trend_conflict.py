"""MT0044 — Daily 4H 1H Trend Conflict. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0044Daily4H1HTrendConflictRule(SpecRule):
    rule_id = "MT0044"
    rule_name = "Daily 4H 1H Trend Conflict"


def evaluate_mt0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0044."""
    return run_spec_rule(MT0044Daily4H1HTrendConflictRule, df)
