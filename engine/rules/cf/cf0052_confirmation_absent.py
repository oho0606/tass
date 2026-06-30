"""CF0052 — Confirmation Absent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0052ConfirmationAbsentRule(SpecRule):
    rule_id = "CF0052"
    rule_name = "Confirmation Absent"


def evaluate_cf0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0052."""
    return run_spec_rule(CF0052ConfirmationAbsentRule, df)
