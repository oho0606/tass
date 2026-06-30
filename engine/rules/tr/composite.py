from __future__ import annotations

from engine.core.types import RuleResult, RuleVerdict

_ATOMIC_KEYS = ("TR0001", "TR0002", "TR0003", "TR0004")


def _v(result: RuleResult) -> str:
    """Effective status for composite matrix (supports legacy WARN)."""
    if result.verdict == "UNKNOWN":
        return "FAIL"
    return result.status


def _composite_result(
    rule_id: str,
    verdict: RuleVerdict,
    score: float,
    reasons: list[str],
    status: str | None = None,
    **kwargs,
) -> RuleResult:
    st = status or verdict
    return RuleResult(
        rule_id=rule_id,
        verdict=verdict,
        status=st,  # type: ignore[arg-type]
        score=score,
        reasons=reasons,
        **kwargs,
    )


def evaluate_trend_structure(atomic: dict[str, RuleResult]) -> RuleResult:
    """TRC001: Trend Structure from atomic rule verdicts."""
    hh = _v(atomic["TR0001"])
    hl = _v(atomic["TR0002"])
    lh = _v(atomic["TR0003"])
    ll = _v(atomic["TR0004"])

    structure_scores = {
        ("PASS", "PASS", "FAIL", "FAIL"): (50.0, "PASS", "Strong Up Trend", "강한 상승 구조"),
        ("PASS", "PASS", "WARN", "FAIL"): (40.0, "PASS", "Up Trend", "상승 추세"),
        ("PASS", "WARN", "WARN", "FAIL"): (30.0, "PASS", "Weak Up Trend", "약한 상승"),
        ("FAIL", "PASS", "PASS", "WARN"): (20.0, "PASS", "Sideways", "횡보 구조"),
        ("FAIL", "FAIL", "PASS", "PASS"): (0.0, "FAIL", "Down Trend", "하락 구조"),
    }

    key = (hh, hl, lh, ll)
    if key in structure_scores:
        score, verdict, state, reason = structure_scores[key]
        status = verdict
    elif all(s == "WARN" for s in key):
        score, verdict, state, reason = 20.0, "PASS", "Neutral", "중립 구조"
        status = "WARN"
    else:
        bullish = sum(1 for s in (hh, hl) if s == "PASS")
        bearish = sum(1 for s in (lh, ll) if s == "FAIL")
        if bullish >= 1 and bearish >= 1:
            score, verdict, state, reason = 25.0, "PASS", "Mixed", "혼합 구조"
            status = "WARN"
        elif bullish >= 2:
            score, verdict, state, reason = 35.0, "PASS", "Up Trend", "상승 우세"
            status = "PASS"
        else:
            score, verdict, state, reason = 10.0, "FAIL", "Weak Down Trend", "약한 하락"
            status = "WARN"

    return _composite_result(
        "TRC001",
        verdict,  # type: ignore[arg-type]
        score,
        [reason],
        status=status,
        confidence_delta=3.0 if verdict == "PASS" else -2.0,
        risk_delta=-2.0 if "Up" in state else 2.0,
        metadata={"trend_state": state},
    )


def evaluate_trend_quality(atomic: dict[str, RuleResult]) -> RuleResult:
    """TRC002: Average atomic quality."""
    scores = [atomic[k].score for k in _ATOMIC_KEYS]
    avg = sum(scores) / len(scores)
    composite = min(50.0, avg * 2.5)

    if composite >= 40:
        verdict, reason = "PASS", "추세 품질 우수"
        status = "PASS"
    elif composite >= 25:
        verdict, reason = "PASS", "추세 품질 보통"
        status = "WARN"
    else:
        verdict, reason = "FAIL", "추세 품질 저하"
        status = "FAIL"

    return _composite_result(
        "TRC002",
        verdict,
        composite,
        [reason],
        status=status,
        metadata={"avg_atomic_score": avg},
    )


def evaluate_trend_continuation(atomic: dict[str, RuleResult]) -> RuleResult:
    """TRC003: Trend continuation based on HH + HL."""
    hh_score = atomic["TR0001"].score
    hl_score = atomic["TR0002"].score
    lh_penalty = max(0, 20 - atomic["TR0003"].score)

    raw = (hh_score + hl_score) / 2 - lh_penalty * 0.3
    score = max(0.0, min(50.0, raw * 2.5))

    if score >= 35:
        verdict, reason, status = "PASS", "추세 지속 신호", "PASS"
    elif score >= 20:
        verdict, reason, status = "PASS", "추세 지속 불확실", "WARN"
    else:
        verdict, reason, status = "FAIL", "추세 지속 실패", "FAIL"

    return _composite_result("TRC003", verdict, score, [reason], status=status)


def evaluate_trend_failure(atomic: dict[str, RuleResult]) -> RuleResult:
    """TRC004: Trend failure detection."""
    lh = atomic["TR0003"]
    ll = atomic["TR0004"]

    failure_signal = (20 - lh.score) + (20 - ll.score)
    score = max(0.0, min(50.0, 50 - failure_signal * 1.25))

    if lh.verdict == "FAIL" or ll.verdict == "FAIL":
        verdict, reason, status = "FAIL", "추세 실패 감지", "FAIL"
    elif score >= 35:
        verdict, reason, status = "PASS", "추세 실패 없음", "PASS"
    else:
        verdict, reason, status = "PASS", "추세 실패 경고", "WARN"

    return _composite_result(
        "TRC004",
        verdict,
        score,
        [reason],
        status=status,
        metadata={"failure_signal": failure_signal},
    )
