"""CMS006 — Swing Structure. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMS006",
    rule_name="Swing Structure",
    atomic_prefix="MS",
    mode="quality",
)


def evaluate_cms006(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMS006 from atomic rule results."""
    return _RULE.evaluate(atomic)
