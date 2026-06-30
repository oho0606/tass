"""CS0044 — Gravestone Doji Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0044GravestoneDojiFormedRule(SpecRule):
    rule_id = "CS0044"
    rule_name = "Gravestone Doji Formed"


def evaluate_cs0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0044."""
    return run_spec_rule(CS0044GravestoneDojiFormedRule, df)
