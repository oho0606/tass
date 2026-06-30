"""CRK003 — Gap Risk. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CRK003",
    rule_name="Gap Risk",
    atomic_prefix="RK",
    mode="bearish",
)


def evaluate_crk003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CRK003 from atomic rule results."""
    return _RULE.evaluate(atomic)
