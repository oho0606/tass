# TASS-006 : Gate Framework

## (Gate 시스템 설계)

**Version:** v0.1.0

**Status:** Draft (MVP-aligned v1.0-rc1)

**Author:** TASS Project

---

## MVP Implementation Notes (v1.0-rc1)

Active gates (`config/gate_pipeline_v1.yaml`):

| Gate | Config key | Effect |
|------|------------|--------|
| Data Quality | `data_quality` | Fail on invalid OHLCV |
| Market | `market` | KOSPI/KOSDAQ regime; `combine_mode: listing` uses symbol market |
| Liquidity | `liquidity` | Min traded value filter |
| Trend | `trend` | Trend floor score |
| Volatility | `volatility` | ATR% warn/fail thresholds |

Recommendation validation composites: CTR001–CTR005, CTR008–CTR010 (`config/recommendation_v1.yaml`).

Gate has priority over total score — unchanged principle.

---

# 1. 목적 (Purpose)

본 문서는 TASS의 Gate(필수 통과 조건) 시스템을 정의한다.

Gate는 단순한 점수 계산이 아니라,

**"이 종목이 추천 자격이 있는가?"**

를 판단하는 시스템이다.

Gate를 통과하지 못한 종목은 총점과 관계없이 추천 대상에서 제외된다.

---

# 2. Gate 철학

점수는 추천 우선순위를 결정한다.

Gate는 추천 자격을 결정한다.

즉,

Gate > Score

이다.

---

# 3. Gate 처리 순서

모든 종목은 아래 순서대로 평가한다.

시장 Gate

↓

유동성 Gate

↓

추세 Gate

↓

변동성 Gate

↓

데이터 품질 Gate

↓

Rule 평가

↓

Score 계산

↓

Confidence 계산

↓

최종 추천

Gate에서 FAIL이 발생하면 이후 단계는 수행하지 않는다.

---

# 4. Gate 종류

현재 TASS v1.0에서는 아래 Gate를 사용한다.

* Market Gate
* Liquidity Gate
* Trend Gate
* Volatility Gate
* Data Quality Gate

추후

* Sector Gate
* Risk Gate
* Market Regime Gate

등을 추가할 수 있다.

---

# 5. Market Gate

목적

시장 전체가 매우 불리한 상황에서는 개별 종목 추천을 제한한다.

평가 예시

* KOSPI 추세
* KOSDAQ 추세
* 시장 변동성
* 시장 위험도

결과

PASS

WARNING

FAIL

WARNING은 추천 가능하지만 감점을 적용한다.

FAIL은 추천 제외.

---

# 6. Liquidity Gate

목적

거래가 어려운 종목을 제거한다.

평가 예시

* 평균 거래대금
* 평균 거래량
* 호가 안정성

결과

PASS

FAIL

FAIL이면 추천 제외.

---

# 7. Trend Gate

목적

장기 하락 추세 종목을 제거한다.

평가 예시

* 장기 이동평균
* 추세 방향
* 고점·저점 구조

결과

PASS

FAIL

FAIL이면 추천 제외.

---

# 8. Volatility Gate

목적

변동성이 과도한 종목을 제거한다.

평가 예시

* ATR
* 최근 변동폭
* 갭 발생 빈도

결과

PASS

WARNING

FAIL

---

# 9. Data Quality Gate

목적

잘못된 데이터로 분석하지 않는다.

검사 항목

* Null
* 중복
* 가격 오류
* 거래량 오류
* 데이터 부족

결과

PASS

FAIL

---

# 10. Gate 우선순위

모든 Gate는 동일하지 않다.

우선순위

1. Data Quality
2. Market
3. Liquidity
4. Trend
5. Volatility

상위 Gate에서 FAIL이 발생하면 즉시 종료한다.

---

# 11. Gate 결과

Gate는 다음 상태만 가진다.

PASS

WARNING

FAIL

PASS

정상 진행

WARNING

계속 진행

감점 적용

FAIL

즉시 종료

추천 제외

---

# 12. Gate와 Score 관계

Gate는 점수를 계산하지 않는다.

Gate는

추천 가능 여부만 판단한다.

점수 계산은 Gate를 통과한 종목에만 수행한다.

---

# 13. Gate 로그

모든 Gate 결과는 기록한다.

예시

Market PASS

Liquidity PASS

Trend FAIL

Result

REJECTED

이 정보는 디버깅과 백테스트에 사용한다.

---

# 14. 예외 처리

Gate는 기본적으로 예외를 허용하지 않는다.

다만 향후 버전에서는

"강한 추세 전환"

등 일부 전략에 한하여 예외 Gate를 둘 수 있다.

---

# 15. AI 설명

추천 제외 시 반드시 이유를 제공한다.

예시

"장기 하락 추세로 인해 Trend Gate를 통과하지 못했습니다."

또는

"평균 거래대금이 기준 이하로 Liquidity Gate를 통과하지 못했습니다."

---

# 16. 백테스트

Gate는 반드시 독립적으로 검증한다.

검증 항목

* 제거 비율
* 제거 후 승률 변화
* 제거 후 손익비 변화
* MDD 개선 효과

효과가 없는 Gate는 수정 또는 제거한다.

---

# 17. 개발 원칙

Gate는

* 단순해야 한다.
* 빠르게 계산되어야 한다.
* 설명 가능해야 한다.
* Python 구현 가능해야 한다.
* 독립 테스트 가능해야 한다.

---

# 18. 향후 확장

추가 예정

* Sector Gate
* ETF Gate
* Earnings Season Gate (선택)
* Multi-Timeframe Gate
* Portfolio Gate

---

# 19. 다음 문서

**TASS-007 : Confidence Framework**

다음 문서에서는

총점과 별도로 계산되는

Confidence(신뢰도)

산출 방식을 정의한다.

---

# 핵심 원칙

Gate는 추천 점수를 높이는 시스템이 아니다.

Gate는 **추천하면 안 되는 종목을 제거하는 시스템**이다.

좋은 종목을 찾기 전에,

나쁜 종목을 먼저 제거하는 것이 TASS의 기본 철학이다.
