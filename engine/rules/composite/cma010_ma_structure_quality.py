"""CMA010 — MA Structure Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMA010",
    rule_name="MA Structure Quality",
    atomic_prefix="MA",
    mode="quality",
)


def evaluate_cma010(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMA010 from atomic rule results."""
    return _RULE.evaluate(atomic)
