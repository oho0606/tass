"""CF0060 — Confirmation Structure Stable. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0060ConfirmationStructureStableRule(SpecRule):
    rule_id = "CF0060"
    rule_name = "Confirmation Structure Stable"


def evaluate_cf0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0060."""
    return run_spec_rule(CF0060ConfirmationStructureStableRule, df)
