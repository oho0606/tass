"""CVO001 — Volatility Compression. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVO001",
    rule_name="Volatility Compression",
    atomic_prefix="VO",
    mode="neutral",
)


def evaluate_cvo001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVO001 from atomic rule results."""
    return _RULE.evaluate(atomic)
