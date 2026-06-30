# TR-001 : Higher High Quality

**Rule ID:** TR-001

**Category:** TR

**Version:** v1.0.0

**Status:** Draft

---

# 1. Purpose

최근 가격 구조에서 Higher High(이전 고점보다 높은 고점)가 형성되었는지 평가하고,

단순 발생 여부가 아닌 **Higher High의 품질(Quality)** 을 점수화한다.

---

# 2. 정의

Higher High란

최근 고점이 직전 고점보다 높게 형성된 상태를 의미한다.

TASS는 Higher High의 개수만 평가하지 않는다.

다음 요소를 함께 평가한다.

* 고점 상승폭
* 연속성
* 거래량 지지
* 추세 유지
* 실패 여부

---

# 3. 목적

이 Rule의 목적은

상승 추세의 첫 번째 조건인

"고점이 계속 높아지고 있는가?"

를 정량적으로 판단하는 것이다.

---

# 4. 입력 데이터

필수

* high_price
* close_price

선택

* volume_shares
* ma_20

---

# 5. 기본 파라미터

Lookback Period

40 Trading Days

Pivot Strength

기본 3

최소 Higher High

2회

---

# 6. 계산 절차

Step 1

최근 40일 데이터 추출

↓

Step 2

Pivot High 탐지

↓

Step 3

Higher High 여부 확인

↓

Step 4

상승폭 계산

↓

Step 5

거래량 확인

↓

Step 6

품질 점수 계산

---

# 7. 평가 요소

① Higher High 개수

② 평균 상승폭

③ 고점 간 간격

④ 거래량 증가 여부

⑤ 추세 유지 여부

⑥ 실패 여부

---

# 8. PASS 조건

다음을 모두 만족

* Higher High 2회 이상
* 평균 상승폭 기준 이상
* 최근 고점이 이전 고점보다 높음
* 추세 유지

---

# 9. WARNING

다음 중 하나

* Higher High는 있으나 상승폭 부족
* 거래량 부족
* 최근 고점 갱신 실패

---

# 10. FAIL

다음 중 하나

* Higher High 없음
* Lower High 발생
* 고점 갱신 실패 반복

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
* Higher High Count
* Average Breakout %
* Quality Grade

---

# 16. 사용자 설명

예시

"최근 40거래일 동안 이전 고점을 지속적으로 돌파하고 있으며, 고점의 질이 양호하여 상승 추세가 유지되고 있습니다."

---

# 17. Python 인터페이스

입력

OHLCV DataFrame

출력

TrendRuleResult

함수명

evaluate_higher_high()

---

# 18. 테스트

필수

* 정상 상승 추세
* 횡보
* 하락 추세
* 급등 후 실패
* 거래량 부족

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

* 뉴스성 급등
* 단기 테마주
* 거래량 왜곡
* 장중 이상 체결

해당 상황은 다른 Rule과 Composite Rule에서 보완한다.

---

# 21. Composite Rule 연결

본 Rule은 다음 Composite Rule에서 사용된다.

* TR-C001 (Trend Structure)
* TR-C002 (Trend Quality)
* TR-C003 (Primary Trend)

---

# 22. 변경 이력

v1.0.0

최초 작성

---

# 핵심 원칙

TR-001은 "Higher High가 있는가?"를 평가하지 않는다.

**"Higher High의 품질(Quality)이 얼마나 우수한가?"를 평가한다.**

이는 TASS의 모든 Trend Rule에 공통으로 적용되는 기본 철학이다.
