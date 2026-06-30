"""CMS010 — Structure Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMS010",
    rule_name="Structure Confirmation",
    atomic_prefix="MS",
    mode="quality",
)


def evaluate_cms010(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMS010 from atomic rule results."""
    return _RULE.evaluate(atomic)
