from __future__ import annotations

from typing import Any

from engine.core.composite_base import BaseCompositeRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.composite._helpers import count_verdicts, effective_verdict

_TREND_ATOMICS = ("TR0001", "TR0002", "TR0003", "TR0004")


class CTR001TrendDirection(BaseCompositeRule):
    rule_id = "CTR001"
    rule_name = "Trend Direction"
    dependencies = _TREND_ATOMICS

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        hh = effective_verdict(atomic["TR0001"])
        hl = effective_verdict(atomic["TR0002"])
        lh = effective_verdict(atomic["TR0003"])
        ll = effective_verdict(atomic["TR0004"])

        bullish = count_verdicts(atomic, ("TR0001", "TR0002"), "PASS")
        bearish = count_verdicts(atomic, ("TR0003", "TR0004"), "FAIL")

        if bullish == 2 and bearish == 0:
            return "PASS", ["상승 추세 방향"], {"direction": "Up"}
        if bearish >= 2 and bullish == 0:
            return "FAIL", ["하락 추세 방향"], {"direction": "Down"}
        if bullish >= 1 and bearish == 0:
            return "PARTIAL", ["약한 상승 방향"], {"direction": "Weak Up"}
        if bearish >= 1 and bullish == 0:
            return "PARTIAL", ["약한 하락 방향"], {"direction": "Weak Down"}
        return "PARTIAL", ["혼합 추세 방향"], {"direction": "Mixed", "signals": (hh, hl, lh, ll)}


class CTR002TrendStrength(BaseCompositeRule):
    rule_id = "CTR002"
    rule_name = "Trend Strength"
    dependencies = _TREND_ATOMICS

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        passed = count_verdicts(atomic, _TREND_ATOMICS, "PASS")
        failed = count_verdicts(atomic, _TREND_ATOMICS, "FAIL")

        if passed >= 3:
            return "PASS", ["추세 강도 높음"], {"pass_count": passed}
        if passed == 2:
            return "PARTIAL", ["추세 강도 보통"], {"pass_count": passed}
        if failed >= 3:
            return "FAIL", ["추세 강도 낮음"], {"fail_count": failed}
        return "PARTIAL", ["추세 강도 불명확"], {"pass_count": passed, "fail_count": failed}


class CTR003TrendQuality(BaseCompositeRule):
    rule_id = "CTR003"
    rule_name = "Trend Quality"
    dependencies = _TREND_ATOMICS

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        hh = effective_verdict(atomic["TR0001"])
        hl = effective_verdict(atomic["TR0002"])

        if hh == "PASS" and hl == "PASS":
            return "PASS", ["추세 품질 우수"], {"quality": "High"}
        if hh == "PASS" or hl == "PASS":
            return "PARTIAL", ["추세 품질 보통"], {"quality": "Medium"}
        return "FAIL", ["추세 품질 저하"], {"quality": "Low"}


class CTR004TrendStability(BaseCompositeRule):
    rule_id = "CTR004"
    rule_name = "Trend Stability"
    dependencies = _TREND_ATOMICS

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        lh = effective_verdict(atomic["TR0003"])
        ll = effective_verdict(atomic["TR0004"])

        if lh == "PASS" and ll == "PASS":
            return "PASS", ["추세 안정"], {"stability": "Stable"}
        if lh == "PASS" or ll == "PASS":
            return "PARTIAL", ["추세 안정성 보통"], {"stability": "Moderate"}
        return "FAIL", ["추세 불안정"], {"stability": "Unstable"}


class CTR005TrendContinuation(BaseCompositeRule):
    rule_id = "CTR005"
    rule_name = "Trend Continuation"
    dependencies = ("TR0001", "TR0002", "TR0003")

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        hh = effective_verdict(atomic["TR0001"])
        hl = effective_verdict(atomic["TR0002"])
        lh = effective_verdict(atomic["TR0003"])

        if hh == "PASS" and hl == "PASS" and lh == "PASS":
            return "PASS", ["추세 지속"], {"continuation": "Strong"}
        if hh == "PASS" and hl == "PASS":
            return "PARTIAL", ["추세 지속 가능"], {"continuation": "Possible"}
        if lh == "FAIL":
            return "FAIL", ["추세 지속 실패"], {"continuation": "Broken"}
        return "PARTIAL", ["추세 지속 불확실"], {"continuation": "Uncertain"}


class CTR006TrendExhaustion(BaseCompositeRule):
    rule_id = "CTR006"
    rule_name = "Trend Exhaustion"
    dependencies = ("TR0003", "TR0004")

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        lh = effective_verdict(atomic["TR0003"])
        ll = effective_verdict(atomic["TR0004"])

        if lh == "FAIL" and ll == "FAIL":
            return "PASS", ["추세 소진 감지"], {"exhaustion": "High"}
        if lh == "FAIL" or ll == "FAIL":
            return "PARTIAL", ["추세 소진 경고"], {"exhaustion": "Moderate"}
        return "FAIL", ["추세 소진 없음"], {"exhaustion": "None"}


class CTR007TrendReversal(BaseCompositeRule):
    rule_id = "CTR007"
    rule_name = "Trend Reversal"
    dependencies = _TREND_ATOMICS

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        hh = effective_verdict(atomic["TR0001"])
        hl = effective_verdict(atomic["TR0002"])
        lh = effective_verdict(atomic["TR0003"])
        ll = effective_verdict(atomic["TR0004"])

        bullish = hh == "PASS" and hl == "PASS"
        bearish = lh == "FAIL" and ll == "FAIL"

        if bullish and bearish:
            return "PARTIAL", ["상반 신호 — 전환 가능"], {"reversal": "Possible"}
        if (hh == "FAIL" and hl == "FAIL") and (lh == "PASS" and ll == "PASS"):
            return "PASS", ["하락에서 상승 전환"], {"reversal": "Bullish"}
        if bullish or bearish:
            return "FAIL", ["추세 전환 미감지"], {"reversal": "None"}
        return "PARTIAL", ["전환 신호 혼재"], {"reversal": "Mixed"}


class CTR008TrendAcceleration(BaseCompositeRule):
    rule_id = "CTR008"
    rule_name = "Trend Acceleration"
    dependencies = ("TR0001", "TR0002")

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        hh = atomic["TR0001"]
        hl = atomic["TR0002"]

        if hh.verdict == "PASS" and hl.verdict == "PASS":
            hh_count = hh.metadata.get("structure_count", 0)
            hl_count = hl.metadata.get("structure_count", 0)
            if hh_count >= 3 and hl_count >= 3:
                return "PASS", ["추세 가속"], {"acceleration": "High"}
            return "PARTIAL", ["추세 가속 초기"], {"acceleration": "Moderate"}
        return "FAIL", ["추세 가속 없음"], {"acceleration": "None"}


class CTR009TrendConsistency(BaseCompositeRule):
    rule_id = "CTR009"
    rule_name = "Trend Consistency"
    dependencies = _TREND_ATOMICS

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        verdicts = [effective_verdict(atomic[rid]) for rid in _TREND_ATOMICS]
        pass_count = verdicts.count("PASS")
        fail_count = verdicts.count("FAIL")

        if pass_count == 4 or fail_count == 4:
            return "PASS", ["추세 일관성 높음"], {"consistency": "High"}
        if pass_count >= 3 or fail_count >= 3:
            return "PARTIAL", ["추세 일관성 보통"], {"consistency": "Medium"}
        return "FAIL", ["추세 일관성 낮음"], {"consistency": "Low"}


class CTR010TrendConfirmation(BaseCompositeRule):
    rule_id = "CTR010"
    rule_name = "Trend Confirmation"
    dependencies = _TREND_ATOMICS

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        bullish = count_verdicts(atomic, ("TR0001", "TR0002"), "PASS")
        bearish_clear = count_verdicts(atomic, ("TR0003", "TR0004"), "PASS")

        if bullish == 2 and bearish_clear == 2:
            return "PASS", ["추세 확인 완료"], {"confirmation": "Full"}
        if bullish >= 1 and bearish_clear >= 1:
            return "PARTIAL", ["추세 부분 확인"], {"confirmation": "Partial"}
        return "FAIL", ["추세 미확인"], {"confirmation": "None"}


_CTR_RULES: tuple[BaseCompositeRule, ...] = (
    CTR001TrendDirection(),
    CTR002TrendStrength(),
    CTR003TrendQuality(),
    CTR004TrendStability(),
    CTR005TrendContinuation(),
    CTR006TrendExhaustion(),
    CTR007TrendReversal(),
    CTR008TrendAcceleration(),
    CTR009TrendConsistency(),
    CTR010TrendConfirmation(),
)


def evaluate_ctr_rules(atomic: dict[str, RuleResult]) -> dict[str, RuleResult]:
    return {rule.rule_id: rule.evaluate(atomic) for rule in _CTR_RULES}


def evaluate_ctr001(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR001TrendDirection().evaluate(atomic)


def evaluate_ctr002(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR002TrendStrength().evaluate(atomic)


def evaluate_ctr003(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR003TrendQuality().evaluate(atomic)


def evaluate_ctr004(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR004TrendStability().evaluate(atomic)


def evaluate_ctr005(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR005TrendContinuation().evaluate(atomic)


def evaluate_ctr006(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR006TrendExhaustion().evaluate(atomic)


def evaluate_ctr007(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR007TrendReversal().evaluate(atomic)


def evaluate_ctr008(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR008TrendAcceleration().evaluate(atomic)


def evaluate_ctr009(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR009TrendConsistency().evaluate(atomic)


def evaluate_ctr010(atomic: dict[str, RuleResult]) -> RuleResult:
    return CTR010TrendConfirmation().evaluate(atomic)
