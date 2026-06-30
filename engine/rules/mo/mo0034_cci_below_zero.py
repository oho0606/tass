"""MO0034 — CCI Below Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0034CCIBelowZeroRule(SpecRule):
    rule_id = "MO0034"
    rule_name = "CCI Below Zero"


def evaluate_mo0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0034."""
    return run_spec_rule(MO0034CCIBelowZeroRule, df)
