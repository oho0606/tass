# TREND-C002 : Trend Quality

**Composite Rule ID:** TREND-C002

**Category:** TREND

**Type:** Composite Rule

**Version:** v1.0.0

**Status:** Draft

---

# 1. Purpose

TREND-C002는 현재 형성된 추세의 **품질(Quality)** 을 정량적으로 평가한다.

추세가 존재하는 것과 좋은 추세인 것은 다르다.

본 Rule은 TASS가 추천할 만한 건강한 추세인지를 판단한다.

---

# 2. Philosophy

좋은 추세는 단순히 가격이 상승하는 것이 아니다.

좋은 추세는 다음 요소가 동시에 만족되어야 한다.

* 구조가 유지된다.
* 거래량이 지지한다.
* 변동성이 안정적이다.
* 조정이 건강하다.
* 모멘텀이 유지된다.

---

# 3. Dependencies

본 Composite Rule은 다음 Rule의 결과를 사용한다.

필수

* TREND-C001 (Trend Structure)

선택(추후 연동)

* VOL-001 (Volume Expansion)
* MA-001 (Moving Average Alignment)
* MOM-001 (MACD Momentum)
* MOM-002 (RSI Strength)
* ATR-001 (ATR Stability)

---

# 4. 평가 요소

Trend Quality는 아래 6개 요소를 평가한다.

① Trend Structure

② Trend Stability

③ Pullback Quality

④ Volume Support

⑤ Momentum Agreement

⑥ Volatility Stability

---

# 5. Trend Structure

TREND-C001 결과를 사용한다.

Strong Up Trend

↓

최고 점수

Weak Up Trend

↓

감점

Neutral 이하

↓

큰 감점

---

# 6. Trend Stability

추세가 얼마나 안정적으로 유지되는지 평가한다.

평가 항목

* 추세 유지 기간

* 연속 Higher High

* 연속 Higher Low

* 추세 붕괴 여부

---

# 7. Pullback Quality

조정의 질을 평가한다.

좋은 조정

* 얕은 눌림

* 거래량 감소

* 이동평균 지지

나쁜 조정

* 깊은 하락

* 거래량 증가

* 지지선 붕괴

---

# 8. Volume Support

거래량이 추세를 지지하는지 평가한다.

예시

상승

*

거래량 증가

↓

가산점

상승

*

거래량 감소

↓

감점

---

# 9. Momentum Agreement

모멘텀이 추세와 같은 방향인지 평가한다.

예시

MACD 상승

*

RSI 정상

↓

가산점

MACD 하락

*

RSI 과열

↓

감점

---

# 10. Volatility Stability

ATR 및 변동성을 평가한다.

건강한 추세

* 일정한 변동성

과도한 추세

* 급등

* 급락

↓

감점

---

# 11. Quality Matrix

| 요소              | 최대점수 |
| --------------- | ---: |
| Trend Structure |   15 |
| Stability       |   10 |
| Pullback        |   10 |
| Volume          |    5 |
| Momentum        |    5 |
| Volatility      |    5 |

총점

50점

---

# 12. Quality Grade

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

+5%

Strong

+4%

Good

+2%

Weak

-3%

Poor

-8%

---

# 14. Risk 영향

Excellent

-5

Strong

-3

Good

-2

Weak

+3

Poor

+8

---

# 15. Gate 관계

Trend Gate에서 참고 Rule로 사용한다.

단독으로 FAIL을 결정하지 않는다.

Trend Score 계산에 반영한다.

---

# 16. 출력값

* Trend Quality Score
* Quality Grade
* Confidence Impact
* Risk Impact
* Strength Summary
* Weakness Summary

---

# 17. 사용자 설명

Excellent

"추세 구조가 안정적으로 유지되고 있으며, 거래량과 모멘텀이 상승을 지지하고 있습니다."

Good

"전반적인 추세는 양호하지만 일부 지표에서 약화 신호가 확인됩니다."

Poor

"추세의 구조와 품질이 모두 약화되어 추천 우선순위가 낮습니다."

---

# 18. Python Interface

입력

CompositeTrendInput

출력

TrendQualityResult

함수명

evaluate_trend_quality()

---

# 19. Backtest

검증 항목

* 승률

* 평균 수익률

* 평균 보유 기간

* MDD

* Profit Factor

* Sharpe Ratio

Quality Grade별 성과를 반드시 비교한다.

---

# 20. Failure Cases

다음 상황에서는 오판 가능성이 있다.

* 급등 후 단기 조정

* 시장 전체 급락

* 저유동성 종목

* 이벤트성 변동

다른 Composite Rule과 함께 판단한다.

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

추세가 존재한다고 해서 좋은 추세는 아니다.

TREND-C002는

추세의 방향이 아니라

**추세의 품질(Quality)** 을 평가한다.

TASS는 품질이 낮은 추세를 추천하지 않는다.
