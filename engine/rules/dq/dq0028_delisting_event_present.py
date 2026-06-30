"""DQ0028 — Delisting Event Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0028DelistingEventPresentRule(SpecRule):
    rule_id = "DQ0028"
    rule_name = "Delisting Event Present"


def evaluate_dq0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0028."""
    return run_spec_rule(DQ0028DelistingEventPresentRule, df)
