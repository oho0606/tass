"""CPT004 — Bearish Pattern. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPT004",
    rule_name="Bearish Pattern",
    atomic_prefix="PT",
    mode="bearish",
)


def evaluate_cpt004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPT004 from atomic rule results."""
    return _RULE.evaluate(atomic)
