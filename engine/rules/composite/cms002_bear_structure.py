"""CMS002 — Bear Structure. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMS002",
    rule_name="Bear Structure",
    atomic_prefix="MS",
    mode="quality",
)


def evaluate_cms002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMS002 from atomic rule results."""
    return _RULE.evaluate(atomic)
