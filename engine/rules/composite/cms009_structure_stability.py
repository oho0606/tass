"""CMS009 — Structure Stability. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMS009",
    rule_name="Structure Stability",
    atomic_prefix="MS",
    mode="quality",
)


def evaluate_cms009(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMS009 from atomic rule results."""
    return _RULE.evaluate(atomic)
