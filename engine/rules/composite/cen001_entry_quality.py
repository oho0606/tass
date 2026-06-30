"""CEN001 — Entry Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CEN001",
    rule_name="Entry Quality",
    atomic_prefix="EN",
    mode="quality",
)


def evaluate_cen001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CEN001 from atomic rule results."""
    return _RULE.evaluate(atomic)
