"""MS0060 — External Swing Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0060ExternalSwingPresentRule(SpecRule):
    rule_id = "MS0060"
    rule_name = "External Swing Present"


def evaluate_ms0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0060."""
    return run_spec_rule(MS0060ExternalSwingPresentRule, df)
