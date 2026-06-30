"""CF0057 — Confirmation Decreasing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0057ConfirmationDecreasingRule(SpecRule):
    rule_id = "CF0057"
    rule_name = "Confirmation Decreasing"


def evaluate_cf0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0057."""
    return run_spec_rule(CF0057ConfirmationDecreasingRule, df)
