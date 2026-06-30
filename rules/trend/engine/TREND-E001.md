# TREND-E001 : Trend Engine

**Engine ID:** TREND-E001

**Category:** TREND

**Type:** Engine

**Version:** v1.0.0

**Status:** Stable

---

# 1. Purpose

TREND-E001은 모든 Trend Rule을 실행하고 종합하여 하나의 Trend Score를 생성하는 엔진이다.

Trend Engine은 TASS에서 추세를 판단하는 유일한 공식 엔진이다.

모든 추천 시스템은 반드시 Trend Engine의 결과를 사용한다.

---

# 2. Philosophy

Atomic Rule은 사실(Fact)을 판단한다.

Composite Rule은 의미(Meaning)를 만든다.

Trend Engine은 최종 판단(Judgement)을 수행한다.

---

# 3. Input

입력 데이터

* OHLCV
* Moving Average Data
* Volume Data
* ATR
* Market Data

---

# 4. Rule Execution Order

Step 1

Atomic Rules 실행

↓

TREND-001

TREND-002

TREND-003

TREND-004

↓

Step 2

Composite Rules 실행

↓

TREND-C001

TREND-C002

TREND-C003

TREND-C004

↓

Step 3

Trend Engine 계산

↓

Trend Score

Trend Grade

Trend Confidence

Trend Risk

---

# 5. Atomic Rule Weight

| Rule      | Weight |
| --------- | -----: |
| TREND-001 |   1.20 |
| TREND-002 |   1.20 |
| TREND-003 |   1.00 |
| TREND-004 |   1.10 |

※ 초기값이며 백테스트를 통해 조정한다.

---

# 6. Composite Rule Weight

| Rule       | Weight |
| ---------- | -----: |
| TREND-C001 |   1.50 |
| TREND-C002 |   1.30 |
| TREND-C003 |   1.20 |
| TREND-C004 |   1.50 |

---

# 7. Trend Score

Trend Engine은 최대 200점을 생성한다.

| 구분              | 최대점수 |
| --------------- | ---: |
| Atomic Rules    |   80 |
| Composite Rules |  120 |

총점

200점

---

# 8. Trend Grade

| 점수      | 등급 |
| ------- | -- |
| 180~200 | S  |
| 160~179 | A  |
| 140~159 | B  |
| 120~139 | C  |
| 0~119   | D  |

---

# 9. Trend State

Trend Engine은 하나의 상태를 출력한다.

* Strong Up Trend
* Up Trend
* Sideways
* Weak Down Trend
* Down Trend

---

# 10. Confidence 계산

Composite Rule의 결과를 종합하여

Trend Confidence를 계산한다.

범위

0~100%

---

# 11. Risk 계산

Trend Risk를 독립적으로 계산한다.

범위

0~100

높을수록 위험하다.

---

# 12. Gate 연동

Trend Engine은 Trend Gate에 아래 정보를 전달한다.

* Trend Score
* Trend Grade
* Trend Confidence
* Trend Risk

Gate Engine이 최종 PASS / WARNING / FAIL을 결정한다.

---

# 13. Output

TrendResult

포함 정보

* Trend Score
* Trend Grade
* Trend State
* Trend Confidence
* Trend Risk
* Atomic Rule Summary
* Composite Rule Summary

---

# 14. Python Interface

입력

TrendEngineInput

출력

TrendEngineResult

함수명

evaluate_trend_engine()

---

# 15. Backtest

Trend Engine 전체를 검증한다.

측정 항목

* 승률
* 평균 수익률
* MDD
* Profit Factor
* Sharpe Ratio
* CAGR

Atomic Rule이 아닌

Engine 전체 성능을 기준으로 평가한다.

---

# 16. Failure Handling

다음 상황에서는 Trend Engine의 신뢰도를 낮춘다.

* 데이터 부족
* Rule 충돌
* Market Gate WARNING
* Confidence 부족

---

# 17. Used By

* Score Engine
* Gate Engine
* Confidence Engine
* Recommendation Engine
* AI Report Engine

---

# 18. Version Policy

Weight 변경

↓

Backtest

↓

성능 검증

↓

Version Update

모든 변경은 버전 관리한다.

---

# 19. Future Extensions

추가 예정

* Multi-Timeframe Trend Engine
* AI Trend Engine
* Sector Trend Engine
* Adaptive Weight Engine

---

# 20. 핵심 원칙

Trend Engine은 단순히 Rule을 실행하는 시스템이 아니다.

Trend Engine은 여러 Rule의 결과를 종합하여

현재 종목의 추세를 가장 객관적으로 판단하는 TASS의 공식 추세 엔진이다.
