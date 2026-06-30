"""CMS003 — Structure Break. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMS003",
    rule_name="Structure Break",
    atomic_prefix="MS",
    mode="quality",
)


def evaluate_cms003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMS003 from atomic rule results."""
    return _RULE.evaluate(atomic)
