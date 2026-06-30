"""CEN005 — Entry Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CEN005",
    rule_name="Entry Confirmation",
    atomic_prefix="EN",
    mode="quality",
)


def evaluate_cen005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CEN005 from atomic rule results."""
    return _RULE.evaluate(atomic)
