# TR-003 : Lower High Detection

**Rule ID:** TR-003

**Category:** TR

**Version:** v1.0.0

**Status:** Draft

---

# 1. Purpose

최근 가격 구조에서 **Lower High(이전 고점보다 낮은 고점)** 이 형성되었는지 평가한다.

본 Rule의 목적은 상승 추세의 약화 또는 하락 추세 전환 가능성을 조기에 감지하는 것이다.

---

# 2. 정의

Lower High란,

최근 Pivot High가 이전 Pivot High보다 낮게 형성된 상태를 의미한다.

Lower High는 매수세가 이전 고점을 돌파하지 못했다는 의미이며,

상승 추세의 힘이 약해지고 있음을 나타낼 수 있다.

---

# 3. 목적

본 Rule은 다음 사항을 평가한다.

* 상승 추세 약화 여부
* 매수세 감소 여부
* 추세 전환 초기 신호
* 고점 갱신 실패 빈도

---

# 4. 입력 데이터

필수

* high_price
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

최소 비교 Pivot

2개

---

# 6. 계산 절차

Step 1

최근 40거래일 데이터 추출

↓

Step 2

Pivot High 탐지

↓

Step 3

최근 Pivot High와 이전 Pivot High 비교

↓

Step 4

Lower High 발생 여부 계산

↓

Step 5

발생 횟수 및 연속성 평가

↓

Step 6

최종 점수 산출

---

# 7. 평가 요소

① Lower High 발생 여부

② 연속 발생 횟수

③ 고점 하락 폭

④ 거래량 감소 여부

⑤ 이동평균 기울기

⑥ 상승 추세 유지 여부

---

# 8. PASS 조건

본 Rule에서 PASS는

**Lower High가 발생하지 않은 상태**를 의미한다.

조건

* 최근 Pivot High가 이전 Pivot High 이상

* 고점 갱신 성공

* 추세 유지

---

# 9. WARNING

다음 중 하나

* Lower High 1회 발생

* 거래량 감소 동반

* 고점 상승폭 둔화

---

# 10. FAIL

다음 중 하나

* Lower High 연속 발생

* 최근 2회 이상 Lower High

* 상승 추세 붕괴 신호

---

# 11. 점수 기준

| 상태      | Score |
| ------- | ----: |
| PASS    |    20 |
| WARNING |    10 |
| FAIL    |     0 |

※ 본 Rule은 감점 성격의 Rule이다.

---

# 12. Confidence 영향

| 결과      |  변화 |
| ------- | --: |
| PASS    | +3% |
| WARNING | -3% |
| FAIL    | -8% |

---

# 13. Risk 영향

| 결과      | 변화 |
| ------- | -: |
| PASS    | -2 |
| WARNING | +4 |
| FAIL    | +8 |

---

# 14. Gate 관계

Trend Gate의 참고 Rule로 사용한다.

단독으로 Gate FAIL을 결정하지 않는다.

다른 Trend Rule과 함께 종합 판단한다.

---

# 15. 출력값

* Status
* Score
* Confidence Impact
* Risk Impact
* Lower High Count
* Highest Pivot
* Latest Pivot
* Quality Grade

---

# 16. 사용자 설명

PASS

"최근 고점을 지속적으로 갱신하고 있어 상승 추세가 유지되고 있습니다."

WARNING

"최근 고점 갱신이 둔화되고 있어 상승 추세가 약해질 가능성이 있습니다."

FAIL

"최근 이전 고점을 돌파하지 못하는 Lower High가 반복되어 추세 전환 위험이 증가하고 있습니다."

---

# 17. Python 인터페이스

입력

OHLCV DataFrame

출력

TrendRuleResult

함수명

evaluate_lower_high()

---

# 18. 테스트

필수 테스트

* 강한 상승 추세

* 횡보 구간

* 상승 후 약화

* 하락 전환

* V자 반등

---

# 19. 백테스트

검증 항목

* 추세 전환 예측 정확도

* 승률 변화

* 평균 수익률

* MDD 감소 효과

최근 10년

KOSPI

KOSDAQ

기준으로 검증한다.

---

# 20. 실패 사례

다음 상황에서는 오판 가능성이 있다.

* 일시적인 횡보

* 박스권 상단 저항

* 단기 이벤트성 변동

* 저유동성 종목

Composite Rule에서 추가 검증한다.

---

# 21. Composite Rule 연결

본 Rule은 다음 Composite Rule에서 사용된다.

* TR-C001 (Trend Structure)

* TR-C002 (Trend Quality)

* TR-C004 (Trend Weakness)

---

# 22. 변경 이력

v1.0.0

최초 작성

---

# 핵심 원칙

Lower High는 단순한 고점 하락이 아니다.

TASS는 Lower High를 **상승 추세의 약화 신호**로 평가하며,

Higher High, Higher Low, Lower High, Lower Low를 함께 분석하여 전체 추세를 판단한다.
