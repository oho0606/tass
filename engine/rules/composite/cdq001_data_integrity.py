"""CDQ001 — Data Integrity. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CDQ001",
    rule_name="Data Integrity",
    atomic_prefix="DQ",
    mode="quality",
)


def evaluate_cdq001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CDQ001 from atomic rule results."""
    return _RULE.evaluate(atomic)
