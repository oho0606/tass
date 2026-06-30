"""CF0054 — Confirmation Lost. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0054ConfirmationLostRule(SpecRule):
    rule_id = "CF0054"
    rule_name = "Confirmation Lost"


def evaluate_cf0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0054."""
    return run_spec_rule(CF0054ConfirmationLostRule, df)
