"""CRK001 — Overall Risk. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CRK001",
    rule_name="Overall Risk",
    atomic_prefix="RK",
    mode="bearish",
)


def evaluate_crk001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CRK001 from atomic rule results."""
    return _RULE.evaluate(atomic)
