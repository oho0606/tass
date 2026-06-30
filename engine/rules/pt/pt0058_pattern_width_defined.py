"""PT0058 — Pattern Width Defined. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0058PatternWidthDefinedRule(SpecRule):
    rule_id = "PT0058"
    rule_name = "Pattern Width Defined"


def evaluate_pt0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0058."""
    return run_spec_rule(PT0058PatternWidthDefinedRule, df)
