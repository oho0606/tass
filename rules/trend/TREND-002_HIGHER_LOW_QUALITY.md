# TREND-002 : Higher Low Quality

**Rule ID:** TREND-002

**Category:** TREND

**Version:** v1.0.0

**Status:** Draft

---

# 1. Purpose

최근 가격 구조에서 Higher Low(이전 저점보다 높은 저점)가 형성되었는지 평가하고,

단순 발생 여부가 아닌 **Higher Low의 품질(Quality)** 을 점수화한다.

Higher Low는 상승 추세의 지속성과 매수세의 방어 능력을 평가하는 핵심 Rule이다.

---

# 2. 정의

Higher Low란,

최근 저점이 직전 저점보다 높게 형성된 상태를 의미한다.

TASS는 단순히 저점이 높아졌는지만 보지 않는다.

다음 요소를 함께 평가한다.

* 저점 상승폭
* 저점 방어력
* 조정의 깊이
* 거래량 특성
* 추세 지속성

---

# 3. 목적

상승 추세에서

"매수세가 이전보다 더 높은 가격에서 유입되는가?"

를 정량적으로 판단한다.

Higher Low는 추세가 건강하게 유지되고 있는지를 평가하는 핵심 기준이다.

---

# 4. 입력 데이터

필수

* low_price
* close_price

선택

* volume_shares
* ma_20
* atr_14

---

# 5. 기본 파라미터

Lookback Period

40 Trading Days

Pivot Strength

기본 3

최소 Higher Low

2회

---

# 6. 계산 절차

Step 1

최근 40거래일 데이터 추출

↓

Step 2

Pivot Low 탐지

↓

Step 3

Higher Low 여부 확인

↓

Step 4

저점 상승폭 계산

↓

Step 5

조정 깊이 계산

↓

Step 6

거래량 확인

↓

Step 7

품질 점수 계산

---

# 7. 평가 요소

① Higher Low 개수

② 평균 저점 상승폭

③ 조정 깊이

④ 거래량 유지 여부

⑤ 추세 지속 여부

⑥ 저점 붕괴 여부

---

# 8. PASS 조건

다음을 모두 만족한다.

* Higher Low 2회 이상
* 최근 저점이 이전 저점보다 높음
* 조정 깊이가 허용 범위 이내
* 추세가 유지됨

---

# 9. WARNING

다음 중 하나

* Higher Low는 있으나 조정이 깊음
* 거래량 감소
* 저점 상승폭 부족

---

# 10. FAIL

다음 중 하나

* Higher Low 없음
* Lower Low 발생
* 최근 저점 붕괴

---

# 11. 점수 기준

| 품질        | Score |
| --------- | ----: |
| Excellent |    20 |
| Strong    |    17 |
| Good      |    14 |
| Weak      |     8 |
| Fail      |     0 |

---

# 12. Confidence 영향

| 결과        |  변화 |
| --------- | --: |
| Excellent | +5% |
| Strong    | +3% |
| Good      | +2% |
| Weak      | -2% |
| Fail      | -5% |

---

# 13. Risk 영향

| 결과        | 변화 |
| --------- | -: |
| Excellent | -5 |
| Strong    | -3 |
| Good      | -2 |
| Weak      | +2 |
| Fail      | +6 |

---

# 14. Gate

Trend Gate의 참고 Rule로 사용한다.

단독 Gate는 아니다.

---

# 15. 출력값

* Status
* Score
* Confidence Impact
* Risk Impact
* Higher Low Count
* Average Pullback %
* Quality Grade

---

# 16. 사용자 설명

예시

"최근 조정 구간에서도 이전보다 높은 가격에서 저점이 형성되어 매수세가 안정적으로 유입되고 있습니다."

---

# 17. Python 인터페이스

입력

OHLCV DataFrame

출력

TrendRuleResult

함수명

evaluate_higher_low()

---

# 18. 테스트

필수

* 정상 상승 추세
* 얕은 눌림목
* 깊은 조정
* 하락 추세
* 거래량 감소

---

# 19. 백테스트

측정 항목

* 승률
* 평균 수익률
* MDD
* Profit Factor
* Sharpe Ratio

최근 10년

KOSPI

KOSDAQ

기준으로 검증한다.

---

# 20. 실패 사례

다음 상황에서는 오판 가능성이 있다.

* 급격한 V자 반등
* 뉴스성 반등
* 단기 과매도 기술적 반등
* 저유동성 종목

다른 Rule과 Composite Rule에서 보완한다.

---

# 21. Composite Rule 연결

본 Rule은 다음 Composite Rule에서 사용된다.

* TREND-C001 (Trend Structure)
* TREND-C002 (Trend Quality)
* TREND-C003 (Primary Trend)

---

# 22. 변경 이력

v1.0.0

최초 작성

---

# 핵심 원칙

TREND-002는 "Higher Low가 있는가?"를 평가하지 않는다.

**"Higher Low의 품질(Quality)이 얼마나 우수한가?"를 평가한다.**

Higher High와 Higher Low는 함께 사용될 때 비로소 건강한 상승 추세를 정의할 수 있다.
