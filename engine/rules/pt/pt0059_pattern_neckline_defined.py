"""PT0059 — Pattern Neckline Defined. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0059PatternNecklineDefinedRule(SpecRule):
    rule_id = "PT0059"
    rule_name = "Pattern Neckline Defined"


def evaluate_pt0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0059."""
    return run_spec_rule(PT0059PatternNecklineDefinedRule, df)
