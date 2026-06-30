# TREND-004 : Lower Low Quality

**Rule ID:** TREND-004

**Category:** TREND

**Version:** v1.0.0

**Status:** Draft

---

# 1. Purpose

최근 가격 구조에서 **Lower Low(이전 저점보다 낮은 저점)** 이 형성되었는지 평가한다.

본 Rule의 목적은 단순한 저점 하락이 아닌,

**하락 추세의 강도와 지속 가능성**을 정량적으로 평가하는 것이다.

---

# 2. 정의

Lower Low란,

최근 Pivot Low가 이전 Pivot Low보다 낮게 형성된 상태를 의미한다.

TASS는 Lower Low 발생 여부만 판단하지 않는다.

다음 요소를 함께 평가한다.

* 저점 하락폭
* 연속성
* 거래량
* 추세 붕괴 정도
* 회복 여부

---

# 3. 목적

다음을 평가한다.

* 상승 추세 종료 여부
* 하락 추세 시작 가능성
* 매도 압력 증가
* 지지선 붕괴

---

# 4. 입력 데이터

필수

* low_price
* close_price

선택

* volume_shares
* ma_20
* ma_60
* atr_14

---

# 5. 기본 파라미터

Lookback Period

40 Trading Days

Pivot Strength

3

최소 Pivot

2개

---

# 6. 계산 절차

Step 1

최근 40일 데이터 추출

↓

Step 2

Pivot Low 탐지

↓

Step 3

Lower Low 확인

↓

Step 4

하락폭 계산

↓

Step 5

거래량 비교

↓

Step 6

회복 여부 확인

↓

Step 7

품질 점수 계산

---

# 7. 평가 요소

① Lower Low 발생 횟수

② 평균 하락폭

③ 연속 발생 여부

④ 거래량 증가 여부

⑤ 이동평균 이탈

⑥ 회복 실패 여부

---

# 8. PASS 조건

PASS는

Lower Low가 발생하지 않았거나,

발생 후 즉시 회복된 경우를 의미한다.

조건

* Lower Low 없음

또는

* 일시적 이탈 후 회복

---

# 9. WARNING

다음 중 하나

* Lower Low 1회

* 거래량 증가 없이 하락

* 저점 이탈 후 회복 중

---

# 10. FAIL

다음 중 하나

* Lower Low 연속 발생

* 거래량 증가와 함께 하락

* 이동평균 이탈

* 회복 실패

---

# 11. 점수 기준

| 상태      | Score |
| ------- | ----: |
| PASS    |    20 |
| WARNING |    10 |
| FAIL    |     0 |

※ 감점 Rule

---

# 12. Confidence 영향

| 결과      |   변화 |
| ------- | ---: |
| PASS    |  +3% |
| WARNING |  -4% |
| FAIL    | -10% |

---

# 13. Risk 영향

| 결과      |  변화 |
| ------- | --: |
| PASS    |  -3 |
| WARNING |  +5 |
| FAIL    | +10 |

---

# 14. Gate 관계

Trend Gate의 핵심 참고 Rule이다.

TREND-003과 함께 상승 추세 붕괴 여부를 판단한다.

---

# 15. 출력값

* Status
* Score
* Confidence Impact
* Risk Impact
* Lower Low Count
* Average Breakdown %
* Recovery Status
* Quality Grade

---

# 16. 사용자 설명

PASS

"최근 저점이 안정적으로 유지되고 있으며 하락 추세 신호는 없습니다."

WARNING

"최근 저점이 일부 이탈하였으나 추세 회복 가능성이 남아 있습니다."

FAIL

"최근 Lower Low가 반복적으로 발생하고 있으며 상승 추세가 붕괴될 가능성이 높습니다."

---

# 17. Python 인터페이스

입력

OHLCV DataFrame

출력

TrendRuleResult

함수명

evaluate_lower_low()

---

# 18. 테스트

필수

* 정상 상승 추세

* 건강한 눌림목

* V자 반등

* 하락 추세

* 급락 후 횡보

* 거래량 증가 하락

---

# 19. 백테스트

검증 항목

* 추세 붕괴 탐지율

* 손실 회피율

* MDD 감소 효과

* 승률 변화

* 평균 수익률

최근 10년

KOSPI

KOSDAQ

기준으로 검증한다.

---

# 20. 실패 사례

오판 가능 상황

* 장중 일시적 급락

* 시장 전체 급락

* 뉴스성 급락

* 저유동성 종목

Composite Rule에서 추가 보완한다.

---

# 21. Composite Rule 연결

본 Rule은 다음 Composite Rule에서 사용된다.

* TREND-C001 (Trend Structure)

* TREND-C002 (Trend Quality)

* TREND-C004 (Trend Failure)

---

# 22. 변경 이력

v1.0.0

최초 작성

---

# 핵심 원칙

TREND-004는 단순히 Lower Low 발생을 평가하지 않는다.

**Lower Low의 품질(Quality)와 추세 붕괴 가능성을 평가하는 Rule이다.**

TREND-001(Higher High), TREND-002(Higher Low), TREND-003(Lower High), TREND-004(Lower Low)는

TASS Trend Engine의 가장 기본이 되는 4개의 Atomic Rule이다.
