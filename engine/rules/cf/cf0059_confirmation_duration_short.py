"""CF0059 — Confirmation Duration Short. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0059ConfirmationDurationShortRule(SpecRule):
    rule_id = "CF0059"
    rule_name = "Confirmation Duration Short"


def evaluate_cf0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0059."""
    return run_spec_rule(CF0059ConfirmationDurationShortRule, df)
