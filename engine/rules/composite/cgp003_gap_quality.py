"""CGP003 — Gap Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CGP003",
    rule_name="Gap Quality",
    atomic_prefix="GP",
    mode="quality",
)


def evaluate_cgp003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CGP003 from atomic rule results."""
    return _RULE.evaluate(atomic)
