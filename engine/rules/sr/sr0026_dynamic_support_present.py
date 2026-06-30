"""SR0026 — Dynamic Support Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0026DynamicSupportPresentRule(SpecRule):
    rule_id = "SR0026"
    rule_name = "Dynamic Support Present"


def evaluate_sr0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0026."""
    return run_spec_rule(SR0026DynamicSupportPresentRule, df)
