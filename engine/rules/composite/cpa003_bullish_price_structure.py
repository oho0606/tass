"""CPA003 — Bullish Price Structure. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA003",
    rule_name="Bullish Price Structure",
    atomic_prefix="PA",
    mode="quality",
)


def evaluate_cpa003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA003 from atomic rule results."""
    return _RULE.evaluate(atomic)
