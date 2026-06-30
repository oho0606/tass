# TASS-004 : Rule Framework

## (Rule 작성 표준 명세서)

**Version:** v0.1.0

**Status:** Draft

**Author:** TASS Project

---

# 1. 목적 (Purpose)

본 문서는 TASS에서 사용하는 모든 Rule의 작성 규칙을 정의한다.

모든 기술적 분석 Rule은 본 문서를 기준으로 작성한다.

본 문서를 통해 Rule의 형식을 통일하고, AI와 개발자가 동일한 기준으로 이해하고 구현할 수 있도록 한다.

---

# 2. Rule 설계 원칙

모든 Rule은 다음 원칙을 반드시 만족해야 한다.

* 하나의 Rule은 하나의 목적만 가진다.
* Rule은 반드시 수치로 계산 가능해야 한다.
* Rule은 Python으로 구현 가능해야 한다.
* Rule은 백테스트 가능해야 한다.
* Rule은 설명 가능해야 한다.
* Rule은 독립적으로 테스트 가능해야 한다.
* Rule은 다른 Rule과 중복되지 않아야 한다.

---

# 3. Rule ID 규칙

Rule ID는 아래 형식을 따른다.

예시

TREND-001

TREND-002

MA-001

MA-002

VOLUME-001

MACD-001

RSI-001

BB-001

ATR-001

RISK-001

MARKET-001

---

# 4. Rule 문서 구조

모든 Rule은 반드시 아래 항목을 포함한다.

1. Rule ID

2. Rule Name

3. 목적

4. 설명

5. 입력 데이터

6. 계산 방법

7. 점수

8. 감점 조건

9. Gate 여부

10. 예외 조건

11. 출력 결과

12. 추천 이유

13. 실패 가능성

14. Python 구현 기준

15. 백테스트 기준

16. 변경 이력

---

# 5. Rule 템플릿

모든 Rule은 아래 형식을 사용한다.

---

Rule ID

TREND-001

Rule Name

Higher High Trend

목적

상승 추세 여부 판단

입력 데이터

* high_price
* close_price
* volume
* ma_20

계산 방법

수식 또는 알고리즘

점수

0 ~ 20점

감점

조건 미달 시 감점

Gate

PASS / FAIL 여부

출력

PASS

FAIL

SCORE

추천 이유

사용자에게 설명할 문장

Python 구현 기준

입력

출력

함수명

백테스트 기준

최근 10년

KOSPI

KOSDAQ

---

---

# 6. Rule 분류

Rule는 아래 카테고리로 관리한다.

TREND

이동 추세

MA

이동평균

VOLUME

거래량

MOMENTUM

모멘텀

VOLATILITY

변동성

RISK

리스크

MARKET

시장

ENTRY

진입

EXIT

청산

---

# 7. Rule 점수

모든 Rule은 점수를 가진다.

점수는

0점

부터

최대 점수

까지 가진다.

예시

0

5

10

15

20

연속 점수 또는 구간 점수는 Rule에 따라 정의한다.

---

# 8. Rule 중요도

모든 Rule은 중요도를 가진다.

CRITICAL

필수

HIGH

매우 중요

MEDIUM

중요

LOW

보조

INFO

참고

중요도는 향후 가중치 조정 시 사용한다.

---

# 9. Gate Rule

일부 Rule은 Gate 역할을 수행한다.

Gate Rule은

PASS

FAIL

만 판단한다.

총점보다 우선한다.

예시

시장 강한 하락

↓

FAIL

↓

추천 제외

---

# 10. Composite Rule

여러 Rule을 조합하여 하나의 Rule을 만들 수 있다.

예시

상승 추세

=

Higher High

*

Higher Low

*

MA 상승

*

거래량 증가

Composite Rule도 Rule ID를 가진다.

---

# 11. Rule Dependency

Rule 간 의존성을 명시한다.

예시

MACD Rule

↓

TREND Rule PASS 이후만 평가

RSI Rule

↓

MA Rule PASS 이후 평가

불필요한 계산을 줄이고 충돌을 방지한다.

---

# 12. 설명 가능성(XAI)

모든 Rule은 사용자에게 설명 가능해야 한다.

예시

"20일 이동평균선이 상승 중이며 거래량이 증가하여 상승 추세가 강화되었습니다."

설명은 사람이 이해할 수 있어야 한다.

---

# 13. Python 구현 규칙

모든 Rule은

입력(Input)

출력(Output)

이 명확해야 한다.

예시

Input

DataFrame

Output

RuleResult

Rule 내부에서 다른 Rule을 직접 호출하지 않는다.

---

# 14. 테스트 규칙

모든 Rule은 단위 테스트(Unit Test)를 작성한다.

테스트 항목

정상 데이터

경계값

결측치

예외 데이터

성능

---

# 15. 버전 관리

Rule 수정 시 반드시 기록한다.

예시

v1.0

최초 작성

v1.1

점수 수정

v1.2

조건 수정

---

# 16. 금지 사항

다음은 허용하지 않는다.

* 감으로 만든 Rule
* 구현 불가능한 Rule
* 백테스트 불가능한 Rule
* 중복 Rule
* 설명 불가능한 Rule
* 근거 없는 점수

---

# 17. Rule 개발 순서

모든 Rule은 아래 순서로 개발한다.

1. 목적 정의

2. 데이터 정의

3. 계산식 작성

4. 점수 정의

5. Gate 여부

6. Python 구현

7. 단위 테스트

8. 백테스트

9. 문서화

10. 배포

---

# 18. 완료 기준

하나의 Rule은 다음 조건을 모두 만족해야 완료로 인정한다.

* 문서 작성 완료
* Python 구현 완료
* Unit Test 통과
* 백테스트 완료
* 설명 가능
* CHANGELOG 기록 완료

---

# 19. 다음 단계

이 문서가 완료되면 개별 Rule 개발을 시작한다.

우선순위는 다음과 같다.

1. TREND (추세)

2. MOVING AVERAGE (이동평균)

3. VOLUME (거래량)

4. MOMENTUM (모멘텀)

5. VOLATILITY (변동성)

6. RISK (리스크)

이 순서를 변경하지 않는다.

---

# 핵심 원칙

Rule는 기술적 분석 이론을 그대로 복사하는 것이 아니라,

**TASS의 표준에 맞게 정량화된 규칙으로 재구성한다.**

모든 Rule은 데이터로 증명되고, 백테스트로 검증되며, AI와 사람이 동일하게 이해할 수 있어야 한다.
