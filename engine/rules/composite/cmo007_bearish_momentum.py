"""CMO007 — Bearish Momentum. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMO007",
    rule_name="Bearish Momentum",
    atomic_prefix="MO",
    mode="bearish",
)


def evaluate_cmo007(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMO007 from atomic rule results."""
    return _RULE.evaluate(atomic)
