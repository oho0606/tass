"""CF0051 — Confirmation Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0051ConfirmationPresentRule(SpecRule):
    rule_id = "CF0051"
    rule_name = "Confirmation Present"


def evaluate_cf0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0051."""
    return run_spec_rule(CF0051ConfirmationPresentRule, df)
