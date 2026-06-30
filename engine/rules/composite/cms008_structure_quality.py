"""CMS008 — Structure Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMS008",
    rule_name="Structure Quality",
    atomic_prefix="MS",
    mode="quality",
)


def evaluate_cms008(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMS008 from atomic rule results."""
    return _RULE.evaluate(atomic)
