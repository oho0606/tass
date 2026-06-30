"""CPT005 — Pattern Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPT005",
    rule_name="Pattern Quality",
    atomic_prefix="PT",
    mode="quality",
)


def evaluate_cpt005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPT005 from atomic rule results."""
    return _RULE.evaluate(atomic)
