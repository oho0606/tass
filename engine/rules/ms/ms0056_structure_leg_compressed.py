"""MS0056 — Structure Leg Compressed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0056StructureLegCompressedRule(SpecRule):
    rule_id = "MS0056"
    rule_name = "Structure Leg Compressed"


def evaluate_ms0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0056."""
    return run_spec_rule(MS0056StructureLegCompressedRule, df)
