"""DQ0047 — Stale Quote Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0047StaleQuotePresentRule(SpecRule):
    rule_id = "DQ0047"
    rule_name = "Stale Quote Present"


def evaluate_dq0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0047."""
    return run_spec_rule(DQ0047StaleQuotePresentRule, df)
