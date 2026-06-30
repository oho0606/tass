# TREND-C001 : Trend Structure

**Composite Rule ID:** TREND-C001

**Category:** TREND

**Type:** Composite Rule

**Version:** v1.0.0

**Status:** Draft

---

# 1. Purpose

TREND-C001은

TREND-001

TREND-002

TREND-003

TREND-004

의 결과를 종합하여

현재 추세 구조가

상승

횡보

하락

중

어느 상태인지를 판단한다.

---

# 2. Philosophy

추세는

하나의 Rule로 판단하지 않는다.

추세는

여러 Atomic Rule의

결과를

조합하여

판단한다.

---

# 3. 사용 Rule

TREND-001

Higher High

TREND-002

Higher Low

TREND-003

Lower High

TREND-004

Lower Low

---

# 4. 입력

Atomic Rule Result

↓

Higher High Score

Higher Low Score

Lower High Score

Lower Low Score

---

# 5. 판단 순서

Step 1

TREND-001 확인

↓

Step 2

TREND-002 확인

↓

Step 3

TREND-003 확인

↓

Step 4

TREND-004 확인

↓

Step 5

Trend Structure 계산

---

# 6. Trend Matrix

| HH      | HL      | LH      | LL      | 구조              |
| ------- | ------- | ------- | ------- | --------------- |
| PASS    | PASS    | FAIL    | FAIL    | Strong Up Trend |
| PASS    | PASS    | WARNING | FAIL    | Up Trend        |
| PASS    | WARNING | WARNING | FAIL    | Weak Up Trend   |
| FAIL    | PASS    | PASS    | WARNING | Sideways        |
| FAIL    | FAIL    | PASS    | PASS    | Down Trend      |
| WARNING | WARNING | WARNING | WARNING | Neutral         |

---

# 7. Trend State

허용 상태

Strong Up Trend

Up Trend

Weak Up Trend

Neutral

Weak Down Trend

Down Trend

Strong Down Trend

---

# 8. Score

최대

50점

예시

Strong Up Trend

50

Up Trend

40

Weak Up

30

Neutral

20

Weak Down

10

Down

0

---

# 9. Confidence

Strong Up

+5%

Up

+3%

Neutral

0%

Weak Down

-5%

Down

-10%

---

# 10. Risk

Strong Up

-5

Up

-3

Neutral

0

Weak Down

+5

Down

+10

---

# 11. Gate

Trend Gate에서

핵심 Composite Rule

로 사용한다.

---

# 12. Output

Trend Structure

Trend Score

Confidence Impact

Risk Impact

Trend Stage

---

# 13. Trend Stage

Stage 1

Accumulation

Stage 2

Early Up Trend

Stage 3

Strong Up Trend

Stage 4

Late Trend

Stage 5

Distribution

Stage 6

Down Trend

---

# 14. User Explanation

예시

"최근 Higher High와 Higher Low가 지속적으로 발생하고 있으며 Lower High와 Lower Low는 확인되지 않아 건강한 상승 추세로 판단됩니다."

---

# 15. Python

evaluate_trend_structure()

↓

TrendCompositeResult

---

# 16. Backtest

측정

승률

평균수익

MDD

Trend Accuracy

Trend Duration

---

# 17. Failure

횡보

뉴스 급등

시장 급락

저유동성

Gap

---

# 18. Dependencies

TREND-001

TREND-002

TREND-003

TREND-004

---

# 19. Used By

Trend Engine

Trend Score

Recommendation Engine

---

# 20. 핵심 원칙

추세는

Higher High

하나로

판단하지 않는다.

Atomic Rule을

조합하여

현재 시장 구조를

판단한다.

TREND-C001은

TASS 최초의 Composite Rule이며,

모든 Trend 분석의

출발점이다.
