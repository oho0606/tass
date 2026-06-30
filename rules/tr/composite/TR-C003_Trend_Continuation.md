# TR-C003 : Trend Continuation

**Composite Rule ID:** TR-C003

**Category:** TR

**Type:** Composite Rule

**Version:** v1.0.0

**Status:** Draft

---

# 1. Purpose

TR-C003은 현재 형성된 추세가 앞으로도 지속될 가능성을 평가한다.

본 Rule은 추세의 방향을 판단하지 않는다.

본 Rule의 목적은 **현재 추세의 지속 가능성(Continuation Probability)** 을 정량적으로 평가하는 것이다.

---

# 2. Philosophy

좋은 추세란 단순히 상승하는 추세가 아니다.

좋은 추세는

* 쉽게 무너지지 않고
* 건강한 조정을 반복하며
* 거래량의 지지를 받고
* 지속적으로 Higher High와 Higher Low를 형성한다.

TASS는 이러한 특성을 가진 추세를 "지속 가능한 추세"로 정의한다.

---

# 3. Dependencies

필수

* TR-C001 (Trend Structure)
* TR-C002 (Trend Quality)

선택(향후 연동)

* MA Engine
* Volume Engine
* Momentum Engine
* Volatility Engine

---

# 4. 평가 요소

Trend Continuation은 아래 요소를 종합 평가한다.

① Trend Age

② Pullback Recovery

③ Momentum Persistence

④ Volume Continuity

⑤ Structure Stability

⑥ Trend Exhaustion

---

# 5. Trend Age

추세가 너무 짧으면 신뢰도가 낮다.

추세가 너무 오래 지속되면 피로도가 증가한다.

적절한 기간의 추세를 가장 높게 평가한다.

---

# 6. Pullback Recovery

조정 이후 얼마나 빠르게 회복하는지 평가한다.

평가 항목

* 회복 속도
* 회복 강도
* 거래량 회복

---

# 7. Momentum Persistence

MACD

RSI

Momentum Engine

결과를 활용하여

모멘텀이 유지되는지 평가한다.

---

# 8. Volume Continuity

상승이 지속될수록

거래량이 적절하게 유지되는지 평가한다.

과도한 거래량 폭증은 오히려 감점 요소가 될 수 있다.

---

# 9. Structure Stability

Higher High

Higher Low

구조가 지속적으로 유지되는지 확인한다.

Lower High

Lower Low

발생 시 감점한다.

---

# 10. Trend Exhaustion

추세 피로도를 평가한다.

평가 예시

* 과도한 상승률
* 장기간 이격
* 연속 양봉
* 과열 구간

피로도가 높을수록 Continuation Score를 감소시킨다.

---

# 11. Continuation Matrix

| 요소                   | 최대점수 |
| -------------------- | ---: |
| Trend Age            |   10 |
| Pullback Recovery    |   10 |
| Momentum Persistence |   10 |
| Volume Continuity    |   10 |
| Structure Stability  |    5 |
| Trend Exhaustion     |    5 |

총점

50점

---

# 12. Continuation Grade

| 점수    | 등급        |
| ----- | --------- |
| 46~50 | Excellent |
| 40~45 | Strong    |
| 32~39 | Good      |
| 24~31 | Weak      |
| 0~23  | Poor      |

---

# 13. Confidence 영향

Excellent

+6%

Strong

+4%

Good

+2%

Weak

-3%

Poor

-10%

---

# 14. Risk 영향

Excellent

-6

Strong

-4

Good

-2

Weak

+3

Poor

+10

---

# 15. Gate 관계

Trend Gate의 참고 Rule이다.

단독으로 FAIL을 결정하지 않는다.

Trend Engine의 Continuation Score 계산에 사용한다.

---

# 16. 출력값

* Continuation Score
* Continuation Grade
* Confidence Impact
* Risk Impact
* Trend Age
* Recovery Strength
* Exhaustion Level

---

# 17. 사용자 설명

Excellent

"현재 추세는 건강한 조정과 회복을 반복하며 지속 가능성이 매우 높은 상태입니다."

Good

"추세는 유지되고 있으나 일부 피로 신호가 나타나고 있습니다."

Poor

"추세 지속 가능성이 낮으며 추세 종료 가능성이 증가하고 있습니다."

---

# 18. Python Interface

입력

TrendContinuationInput

출력

TrendContinuationResult

함수명

evaluate_trend_continuation()

---

# 19. Backtest

검증 항목

* 추세 지속 성공률
* 평균 보유 기간
* 평균 수익률
* MDD
* Profit Factor
* Sharpe Ratio

Continuation Grade별 성과를 비교한다.

---

# 20. Failure Cases

다음 상황에서는 오판 가능성이 있다.

* 돌발 악재
* 시장 급변
* 거래정지
* 초저유동성 종목

다른 Engine과 함께 최종 판단한다.

---

# 21. Used By

* Trend Engine
* Score Engine
* Confidence Engine
* Recommendation Engine

---

# 22. Changelog

v1.0.0

최초 작성

---

# 핵심 원칙

TR-C003은 현재 추세를 평가하는 것이 아니다.

**현재 추세가 앞으로도 이어질 가능성**을 평가한다.

TASS는 단기 급등보다 지속 가능한 추세를 우선 추천한다.
