# TASS-002 : Data Specification

## (데이터 명세서)

**Version:** v0.1.0

**Status:** Draft (MVP-aligned v1.0-rc1)

**Author:** TASS Project

---

## MVP Implementation Notes (v1.0-rc1)

| Item | MVP value |
|------|-----------|
| Data source | Yahoo Finance OHLCV (delayed) via `engine/data/` |
| Cache | `data/cache/` — validated by `scripts/validate_cache.py` |
| Universe | `config/universe_krx_mvp.csv` (59 liquid names); bootstrap via `scripts/bootstrap_universe.py` |
| Min bars | 60 (`config/settings.yaml`) |
| Lookback | 400 trading days |
| DQ Gate | `engine/data/validator.py` + cache validation script |

Full KRX listing via PyKRX is supported when network credentials are available (`scripts/generate_universe.py`).

---

# 1. 목적 (Purpose)

본 문서는 TASS 프로젝트에서 사용하는 모든 데이터의 표준을 정의한다.

모든 AI(Cursor, Claude Code, Codex 등), Python 코드, 백테스트, API, 데이터베이스는 반드시 본 문서를 따른다.

본 문서의 목적은 다음과 같다.

* 데이터 표준화
* AI 간 동일한 결과 보장
* Rule 구현 기준 제공
* 백테스트 일관성 유지
* 유지보수 용이성 확보

---

# 2. 데이터 원칙

TASS는 다음 데이터만 사용한다.

## 허용 데이터

### 가격 데이터 (OHLCV)

* Open
* High
* Low
* Close
* Volume

---

### 이동평균

* MA 5
* MA 10
* MA 20
* MA 60
* MA 120
* MA 240

---

### 거래량

* 당일 거래량
* 5일 평균 거래량
* 20일 평균 거래량
* 거래대금
* 거래량 증가율

---

### 추세

* Higher High
* Higher Low
* Lower High
* Lower Low
* 추세 방향
* 추세 강도

---

### 모멘텀

* RSI(14)
* MACD(12,26,9)
* Signal
* Histogram

---

### 변동성

* ATR(14)
* Bollinger Bands(20,2)

---

### 거래량 지표

* OBV
* Volume Ratio

---

### 시장 데이터

* KOSPI
* KOSDAQ

---

# 3. 사용 금지 데이터

TASS는 아래 데이터를 절대로 사용하지 않는다.

* 뉴스
* 공시
* 실적
* 정치
* SNS
* 유튜브
* 커뮤니티
* 테마
* 루머
* 애널리스트 의견

---

# 4. 기본 차트

기본 분석 차트

일봉

보조 차트

주봉

선택 차트

60분봉

30분봉

초기 버전에서는

일봉 중심으로 분석한다.

---

# 5. 기본 기간

## 이동평균

MA 5

MA 10

MA 20

MA 60

MA 120

MA 240

---

## RSI

14

---

## ATR

14

---

## MACD

12

26

9

---

## Bollinger Bands

20

표준편차 2

---

# 6. 표준 변수명

| 변수명            | 타입    | 설명        |
| -------------- | ----- | --------- |
| open_price     | float | 시가        |
| high_price     | float | 고가        |
| low_price      | float | 저가        |
| close_price    | float | 종가        |
| volume_shares  | int   | 거래량       |
| trading_value  | float | 거래대금      |
| ma_5           | float | 5일 이동평균   |
| ma_10          | float | 10일 이동평균  |
| ma_20          | float | 20일 이동평균  |
| ma_60          | float | 60일 이동평균  |
| ma_120         | float | 120일 이동평균 |
| ma_240         | float | 240일 이동평균 |
| rsi_14         | float | RSI       |
| atr_14         | float | ATR       |
| macd           | float | MACD      |
| macd_signal    | float | Signal    |
| macd_histogram | float | Histogram |
| obv            | float | OBV       |
| bb_upper       | float | 볼린저 상단    |
| bb_middle      | float | 볼린저 중앙    |
| bb_lower       | float | 볼린저 하단    |

---

# 7. 데이터 타입

가격

float

거래량

int

비율

float

점수

int

날짜

datetime

종목코드

string

종목명

string

---

# 8. 데이터 최소 요구사항

Rule 계산을 위해

최소

240 거래일

데이터 확보

권장

500 거래일

이상

---

# 9. 데이터 업데이트

추천

매일 장 종료 후

1회 업데이트

추후

실시간 업데이트 지원 가능

---

# 10. 데이터 품질 기준

누락 데이터

허용하지 않음

이상치 발생

자동 검증

중복 데이터

자동 제거

데이터 순서

오름차순 날짜

---

# 11. 데이터 소스

현재

미정

향후 지원 예정

* KIS Open API
* 키움 API
* 한국거래소
* Yahoo Finance (보조)
* 기타 API

중요

데이터 소스가 변경되어도

TASS 내부 데이터 구조는 변경하지 않는다.

---

# 12. Data Adapter

모든 외부 데이터는

Data Adapter를 통해

TASS 표준으로 변환한다.

예시

KIS

↓

Data Adapter

↓

TASS Data

↓

Engine

---

# 13. 데이터 흐름

외부 API

↓

Data Adapter

↓

Validation

↓

Database

↓

Indicator Engine

↓

Rule Engine

↓

Scoring Engine

↓

Recommendation Engine

↓

Frontend

---

# 14. 데이터 검증

모든 데이터는

다음 항목을 검증한다.

* Null 여부
* 음수 가격 여부
* 거래량 오류
* 날짜 중복
* 정렬 여부
* 결측치

---

# 15. AI 개발 원칙

모든 AI는

반드시 본 문서를 기준으로 개발한다.

임의의 변수명을 생성하지 않는다.

임의의 이동평균 기간을 사용하지 않는다.

임의의 RSI 기간을 사용하지 않는다.

본 문서가 데이터 표준이다.

---

# 16. 향후 확장

추후 추가 예정

* VWAP
* ADX
* DMI
* Relative Strength
* Relative Volume
* SuperTrend
* Donchian Channel
* Keltner Channel
* Chaikin Money Flow
* MFI

추가되더라도

기존 구조는 변경하지 않는다.

---

# 17. 다음 문서

다음 개발 문서

**TASS-003 : System Architecture**

TASS의 전체 시스템 구조를 정의한다.

Engine 간의 관계

API 구조

Backend

Frontend

Database

Recommendation Engine

AI Engine

Scoring Engine

모든 구조를 정의한다.

---

# 핵심 원칙

**데이터는 프로젝트의 언어(Language)이다.**

모든 Rule, Engine, API, AI, Database는 반드시 동일한 데이터 표준을 사용해야 한다.

데이터가 표준화되어야 백테스트, 추천 결과, AI 분석이 항상 동일한 결과를 생성할 수 있다.
