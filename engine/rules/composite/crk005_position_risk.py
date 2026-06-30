"""CRK005 — Position Risk. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CRK005",
    rule_name="Position Risk",
    atomic_prefix="RK",
    mode="bearish",
)


def evaluate_crk005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CRK005 from atomic rule results."""
    return _RULE.evaluate(atomic)
