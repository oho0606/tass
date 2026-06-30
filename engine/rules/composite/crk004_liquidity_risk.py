"""CRK004 — Liquidity Risk. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CRK004",
    rule_name="Liquidity Risk",
    atomic_prefix="RK",
    mode="bearish",
)


def evaluate_crk004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CRK004 from atomic rule results."""
    return _RULE.evaluate(atomic)
