"""CF0058 — Confirmation Duration Long. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0058ConfirmationDurationLongRule(SpecRule):
    rule_id = "CF0058"
    rule_name = "Confirmation Duration Long"


def evaluate_cf0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0058."""
    return run_spec_rule(CF0058ConfirmationDurationLongRule, df)
