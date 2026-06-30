"""CPA004 — Bearish Price Structure. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA004",
    rule_name="Bearish Price Structure",
    atomic_prefix="PA",
    mode="bearish",
)


def evaluate_cpa004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA004 from atomic rule results."""
    return _RULE.evaluate(atomic)
