from __future__ import annotations

from engine.core.types import RuleResult, RuleVerdict


def effective_verdict(result: RuleResult) -> RuleVerdict:
    return result.verdict


def count_verdicts(
    atomic: dict[str, RuleResult], rule_ids: tuple[str, ...], verdict: RuleVerdict
) -> int:
    return sum(1 for rid in rule_ids if effective_verdict(atomic[rid]) == verdict)


def composite_result(
    rule_id: str,
    verdict: RuleVerdict,
    reasons: list[str],
    **metadata,
) -> RuleResult:
    return RuleResult(
        rule_id=rule_id,
        verdict=verdict,
        status=verdict,
        score=0.0,
        reasons=reasons,
        metadata=metadata,
    )


def verdict_from_ratio(
    passed: int, partial: int, failed: int, *, pass_min: int, partial_min: int
) -> RuleVerdict:
    if passed >= pass_min:
        return "PASS"
    if passed + partial >= partial_min:
        return "PARTIAL"
    if failed > passed:
        return "FAIL"
    return "PARTIAL"
