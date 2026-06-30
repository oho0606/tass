# TR-C004 : Trend Failure

**Composite Rule ID:** TR-C004

**Category:** TR

**Type:** Composite Rule

**Version:** v1.0.0

**Status:** Draft

---

# 1. Purpose

TR-C004는 현재 상승 추세가 종료되었는지 또는 종료될 가능성이 높은지를 평가한다.

본 Rule은 새로운 매수를 차단하고,

기존 추천 종목의 위험도를 높이는 핵심 Composite Rule이다.

---

# 2. Philosophy

추세는 시작보다 종료를 정확히 판단하는 것이 더 중요하다.

Trend Failure는

하락을 예측하는 것이 아니라,

상승 추세의 붕괴 가능성을 정량적으로 평가한다.

---

# 3. Dependencies

필수

TR-C001

Trend Structure

TR-C002

Trend Quality

TR-C003

Trend Continuation

추후 연동

MA Engine

Momentum Engine

Volume Engine

Risk Engine

---

# 4. Failure Components

Trend Failure는

아래 6가지 요소를 평가한다.

① Structure Failure

② Moving Average Failure

③ Momentum Failure

④ Volume Failure

⑤ Volatility Failure

⑥ Recovery Failure

---

# 5. Structure Failure

평가 항목

* Lower High

* Lower Low

* Higher Low 붕괴

* Pivot Failure

구조 붕괴가 반복될수록

Failure Score 증가

---

# 6. Moving Average Failure

평가 항목

* MA20 이탈

* MA60 이탈

* 정배열 붕괴

* 이동평균 기울기 감소

---

# 7. Momentum Failure

평가 항목

* MACD 약세 전환

* RSI 약화

* Momentum Divergence

---

# 8. Volume Failure

평가 항목

* 상승 시 거래량 감소

* 하락 시 거래량 증가

* Distribution 의심

---

# 9. Volatility Failure

평가 항목

* ATR 급증

* 장대 음봉

* Gap Down

* 변동성 급격한 확대

---

# 10. Recovery Failure

하락 이후

회복 실패 여부

평가

* 반등 실패

* 저점 갱신

* 회복 속도

---

# 11. Failure Matrix

| 요소             | 최대점수 |
| -------------- | ---: |
| Structure      |   15 |
| Moving Average |   10 |
| Momentum       |   10 |
| Volume         |    5 |
| Volatility     |    5 |
| Recovery       |    5 |

총점

50점

※ 점수가 높을수록 Failure 위험이 높다.

---

# 12. Failure Grade

| 점수    | 등급       |
| ----- | -------- |
| 0~10  | Very Low |
| 11~20 | Low      |
| 21~30 | Moderate |
| 31~40 | High     |
| 41~50 | Critical |

---

# 13. Confidence 영향

| 등급       |   영향 |
| -------- | ---: |
| Very Low |  +2% |
| Low      |   0% |
| Moderate |  -3% |
| High     |  -6% |
| Critical | -12% |

---

# 14. Risk 영향

| 등급       |  변화 |
| -------- | --: |
| Very Low |  -2 |
| Low      |   0 |
| Moderate |  +4 |
| High     |  +8 |
| Critical | +15 |

---

# 15. Gate 관계

Trend Gate의 핵심 Composite Rule이다.

Critical 등급은

Trend Gate FAIL 후보로 전달한다.

최종 FAIL 여부는 Gate Engine에서 결정한다.

---

# 16. 출력값

* Failure Score
* Failure Grade
* Failure Components
* Confidence Impact
* Risk Impact
* Gate Recommendation

---

# 17. 사용자 설명

Very Low

"현재 상승 추세는 안정적으로 유지되고 있습니다."

Moderate

"추세 약화 신호가 일부 확인되고 있으므로 주의가 필요합니다."

Critical

"상승 추세가 붕괴될 가능성이 매우 높습니다. 신규 진입을 권장하지 않습니다."

---

# 18. Python Interface

입력

TrendFailureInput

출력

TrendFailureResult

함수명

evaluate_trend_failure()

---

# 19. Backtest

검증 항목

* 추세 종료 탐지율

* 손실 회피율

* MDD 감소 효과

* Profit Factor 개선

* 평균 보유 기간 최적화

최근 10년

KOSPI

KOSDAQ

기준으로 검증한다.

---

# 20. Failure Cases

다음 상황에서는 오판 가능성이 있다.

* 시장 전체 급락

* 단기 이벤트

* 실적 발표

* 거래정지

* 초저유동성 종목

다른 Engine과 함께 최종 판단한다.

---

# 21. Used By

* Trend Engine

* Gate Engine

* Risk Engine

* Recommendation Engine

---

# 22. Changelog

v1.0.0

최초 작성

---

# 핵심 원칙

TR-C004는

하락을 예측하는 Rule이 아니다.

**현재 상승 추세를 더 이상 신뢰할 수 있는지 평가하는 Rule**이다.

Trend Failure가 높다고 반드시 하락하는 것은 아니지만,

TASS는 위험이 커진 종목보다 건강한 추세를 우선 추천한다.
