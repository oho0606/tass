# TASS-005 : Scoring Framework

## (점수 체계 설계)

**Version:** v0.1.0

**Status:** Draft (MVP-aligned v1.0-rc1)

**Author:** TASS Project

---

## MVP Implementation Notes (v1.0-rc1)

| Mode | Max score | Active domains |
|------|----------:|----------------|
| MVP (`mvp_mode: true`) | **500** | Trend 200, MA 150, Volume 150 |
| Full (`mvp_mode: false`) | **1000** | All 16 domain engines |

MVP operational rules: `config/mvp_operational_rules.yaml` (26 rules).

Score normalization for recommendation: MVP scores are scaled to 1000-pt equivalent in `engine/recommendation/normalize.py`.

Thresholds: `config/recommendation_v1.yaml` (calibrated for MVP scale).

---

# 1. 목적 (Purpose)

본 문서는 TASS의 점수 계산 원칙을 정의한다.

점수는 단순히 Rule의 합계가 아니라,

* Rule
* Weight
* Gate
* Confidence

를 종합하여 계산한다.

본 문서는 모든 Rule이 공통으로 사용하는 점수 계산 표준이다.

---

# 2. 점수 철학

TASS는 "좋아 보인다"라는 주관적 표현을 사용하지 않는다.

모든 평가는 숫자로 표현한다.

예시

❌ 상승 추세가 강하다.

✅ 추세 점수 183 / 200

---

# 3. 점수 계산 구조

Raw Rule Score

↓

Category Score

↓

Weighted Score

↓

Gate 적용

↓

Confidence 적용

↓

Final Score

---

# 4. 총점 구조

총점

1000점

| 분야             | 최대점수 |
| -------------- | ---: |
| Market         |  100 |
| Trend          |  200 |
| Moving Average |  150 |
| Volume         |  150 |
| Momentum       |  150 |
| Volatility     |  100 |
| Entry          |   50 |
| Exit           |   50 |
| Risk           |   50 |
| Confidence     |   50 |

합계

1000점

---

# 5. 점수 단계

모든 Rule은

0점

부터

최대 점수

사이를 가진다.

예시

0

5

10

15

20

연속 점수도 허용한다.

예시

17.3점

18.7점

---

# 6. Weight

모든 Rule은 Weight를 가진다.

예시

CRITICAL

×1.50

HIGH

×1.20

NORMAL

×1.00

LOW

×0.80

INFO

×0.50

Weight는 백테스트를 통해 조정한다.

---

# 7. Category Score

Rule 점수는 분야별로 합산한다.

예시

Trend

183 / 200

Moving Average

142 / 150

Volume

136 / 150

---

# 8. Gate

Gate는 점수보다 우선한다.

예시

시장 Gate FAIL

↓

최종 추천 제외

총점이 높아도 Gate FAIL이면 추천하지 않는다.

---

# 9. Confidence

총점과 별도로 신뢰도를 계산한다.

신뢰도는

0~100%

으로 표현한다.

평가 요소

* Rule 일치성
* 추세 일치
* 거래량 일치
* 모멘텀 일치
* 시간프레임 일치

---

# 10. Final Score

최종 평가는

총점과 신뢰도를 함께 사용한다.

예시

총점

918 /1000

신뢰도

94%

등급

S

추천

★★★★★

---

# 11. 등급 기준

| 점수       | 등급    |
| -------- | ----- |
| 950~1000 | S+    |
| 900~949  | S     |
| 850~899  | A+    |
| 800~849  | A     |
| 750~799  | B     |
| 700~749  | C     |
| 700 미만   | 추천 제외 |

※ 위 기준은 초기값이며 백테스트 결과에 따라 조정한다.

---

# 12. 추천 기준

추천은 아래 조건을 모두 만족해야 한다.

* Gate PASS
* 최소 총점 이상
* 최소 Confidence 이상
* 최소 유동성 이상

하나라도 만족하지 못하면 추천하지 않는다.

---

# 13. 감점 원칙

다음 상황에서는 감점한다.

* 지표 충돌
* 거래량 감소
* 변동성 과다
* 시장 약세
* 추세 약화

감점은 중복 적용할 수 있다.

---

# 14. 보너스 점수

다음 조건은 추가 점수를 받을 수 있다.

* 여러 핵심 Rule 동시 충족
* 추세와 거래량 동시 강화
* 다중 시간프레임 일치
* 상대강도 우수

보너스 점수는 최대 분야별 상한을 넘지 않는다.

---

# 15. 동점 처리

동점인 경우 아래 순서로 우선순위를 결정한다.

1. Confidence
2. Trend Score
3. Volume Score
4. Risk Score
5. 거래대금

---

# 16. 출력 형식

최종 결과는 아래 정보를 포함한다.

* 총점
* 분야별 점수
* Confidence
* 등급
* 추천 여부
* 추천 이유
* 감점 이유

---

# 17. 백테스트 원칙

모든 Weight와 점수는 백테스트를 통해 검증한다.

다음 항목을 측정한다.

* 승률
* 평균 수익률
* 평균 손실률
* 손익비
* 최대 낙폭(MDD)
* CAGR

백테스트 결과가 좋지 않으면 Weight를 수정한다.

---

# 18. 절대 원칙

점수는 절대 감으로 수정하지 않는다.

Weight 변경

↓

백테스트

↓

성능 확인

↓

반영

이 과정을 반드시 따른다.

---

# 19. 향후 확장

향후 추가 예정

* Machine Learning Weight
* Adaptive Weight
* Market Regime Weight
* Sector Weight
* AI Dynamic Weight

초기 버전에서는 고정 Weight를 사용한다.

---

# 20. 다음 단계

다음 문서는

**TASS-006 : Gate Framework**

Gate의 종류

Gate 우선순위

탈락 기준

예외 처리

시장 Gate

유동성 Gate

추세 Gate

리스크 Gate

를 정의한다.

---

# 핵심 원칙

**총점은 추천의 조건이지만, Gate는 추천의 자격이다.**

TASS는 점수가 높다고 추천하지 않는다.

반드시 Gate를 통과한 종목만 추천 대상으로 선정한다.
