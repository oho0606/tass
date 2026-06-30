"""DQ0027 — Symbol Change Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0027SymbolChangePresentRule(SpecRule):
    rule_id = "DQ0027"
    rule_name = "Symbol Change Present"


def evaluate_dq0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0027."""
    return run_spec_rule(DQ0027SymbolChangePresentRule, df)
