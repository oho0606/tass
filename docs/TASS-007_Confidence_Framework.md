# TASS-007 : Confidence Framework

## (신뢰도 계산 프레임워크)

**Version:** v0.1.0

**Status:** Draft (MVP-aligned v1.0-rc1)

**Author:** TASS Project

---

## MVP Implementation Notes (v1.0-rc1)

MVP Confidence uses Trend + MA + Volume domain alignment (3 domains).

Implementation: `engine/confidence/` — separate from Master Score.

Recommendation minimum: `confidence_min: 52.0` (`config/recommendation_v1.yaml`).

Full-mode Confidence adds multi-timeframe and additional domain signals (v1.3).

---

# 1. 목적 (Purpose)

본 문서는 TASS의 Confidence(신뢰도) 계산 방식을 정의한다.

Confidence는 점수와 별개의 개념이다.

동일한 점수를 받은 종목이라도 신뢰도는 다를 수 있다.

Confidence는 추천 결과의 안정성과 일관성을 수치화하여 사용자에게 제공한다.

---

# 2. Confidence 철학

점수는 높지만 신뢰도가 낮은 종목은 공격적인 매매 대상이다.

점수도 높고 신뢰도도 높은 종목은 TASS가 가장 우선 추천하는 종목이다.

즉,

Score = 품질

Confidence = 신뢰성

이다.

---

# 3. 계산 구조

Indicator Agreement

↓

Trend Agreement

↓

Volume Agreement

↓

Momentum Agreement

↓

Volatility Agreement

↓

Timeframe Agreement

↓

Confidence Score

---

# 4. 계산 범위

Confidence는

0 ~ 100%

으로 계산한다.

예시

95~100%

매우 높음

85~94%

높음

70~84%

보통

60~69%

낮음

60% 미만

추천 제외 검토

---

# 5. 평가 요소

Confidence는 다음 요소를 종합 평가한다.

* 추세 일치성
* 이동평균 일치성
* 거래량 일치성
* 모멘텀 일치성
* 변동성 적합성
* 다중 시간프레임 일치성
* Rule 충돌 여부

---

# 6. Indicator Agreement

여러 기술적 지표가 동일한 방향을 가리키는지 평가한다.

예시

상승

* MA
* MACD
* RSI
* OBV

모두 상승

↓

Confidence 증가

지표 간 방향이 다르면 Confidence 감소

---

# 7. Trend Agreement

단기 추세와 장기 추세가 같은 방향인지 확인한다.

예시

20일선 상승

60일선 상승

120일선 상승

↓

Confidence 증가

---

# 8. Volume Agreement

거래량이 추세를 지지하는지 확인한다.

예시

가격 상승

*

거래량 증가

↓

Confidence 증가

가격 상승

*

거래량 감소

↓

Confidence 감소

---

# 9. Momentum Agreement

MACD, RSI 등 모멘텀 지표가 같은 방향인지 평가한다.

충돌이 많을수록 Confidence를 낮춘다.

---

# 10. Volatility Agreement

변동성이 전략에 적합한지 평가한다.

과도한 변동성은 Confidence를 감소시킨다.

적절한 변동성은 Confidence를 증가시킨다.

---

# 11. Multi-Timeframe Agreement

기본 시간프레임

일봉

보조 시간프레임

주봉

선택

60분봉

주봉과 일봉의 방향이 일치하면 Confidence를 높인다.

방향이 반대면 Confidence를 낮춘다.

---

# 12. Rule Conflict

Rule 간 충돌을 평가한다.

예시

Trend

PASS

MACD

PASS

RSI

FAIL

↓

Confidence 감소

충돌이 적을수록 Confidence는 높아진다.

---

# 13. Confidence 등급

95~100%

★★★★★

90~94%

★★★★☆

80~89%

★★★★

70~79%

★★★

60~69%

★★

60% 미만

★

---

# 14. 추천 기준

추천은

총점만으로 결정하지 않는다.

다음을 함께 고려한다.

* Gate
* Total Score
* Confidence

예시

Score

940

Confidence

52%

↓

추천 보류

---

# 15. 출력 형식

최종 보고서에는 반드시 포함한다.

* Confidence
* Confidence 등급
* Confidence 증가 요인
* Confidence 감소 요인

---

# 16. 사용자 설명

예시

Confidence 96%

이유

* 장기·단기 추세 일치
* 거래량 증가
* MACD 상승
* RSI 정상
* Rule 충돌 없음

또는

Confidence 68%

이유

* 거래량 감소
* RSI 과열
* 추세와 모멘텀 충돌

---

# 17. 백테스트

Confidence의 효과를 독립적으로 검증한다.

검증 항목

* Confidence별 승률
* Confidence별 평균 수익률
* Confidence별 손익비
* Confidence별 MDD

Confidence 기준이 성능 향상에 기여하지 않으면 수정한다.

---

# 18. 개발 원칙

Confidence는

* 독립적으로 계산한다.
* Score와 혼합하지 않는다.
* Gate와 혼합하지 않는다.
* 항상 설명 가능해야 한다.
* Python으로 구현 가능해야 한다.

---

# 19. 향후 확장

추가 예정

* AI Dynamic Confidence
* Market Regime Confidence
* Sector Confidence
* Portfolio Confidence
* Machine Learning Confidence

---

# 20. 다음 문서

**TASS-008 : Risk Management Framework**

다음 문서에서는

* 손절 전략
* 익절 전략
* 포지션 크기
* 최대 손실
* 리스크 관리 원칙

을 정의한다.

---

# 핵심 원칙

높은 점수는 좋은 종목을 의미한다.

높은 Confidence는 그 판단을 믿을 수 있음을 의미한다.

TASS는 Score와 Confidence를 함께 사용하여 최종 추천을 결정한다.
