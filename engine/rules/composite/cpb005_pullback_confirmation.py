"""CPB005 — Pullback Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPB005",
    rule_name="Pullback Confirmation",
    atomic_prefix="PB",
    mode="quality",
)


def evaluate_cpb005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPB005 from atomic rule results."""
    return _RULE.evaluate(atomic)
