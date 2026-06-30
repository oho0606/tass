# TASS-003 : System Architecture

## (시스템 아키텍처)

**Version:** v0.1.0

**Status:** Draft (MVP-aligned v1.0-rc1)

**Author:** TASS Project

---

## MVP Implementation Notes (v1.0-rc1)

```text
Frontend (Next.js) → API (FastAPI) → Application Layer (TASS-032)
  → RecommendationService / BacktestService
  → Engine (Data → Indicator → Domain Engines → Score → Gate → Recommendation)
  → JSON output / API response
```

| Layer | Path | Status |
|-------|------|--------|
| Engine | `engine/` | MVP 3-domain pipeline active |
| API | `api/` | REST BFF for picks, health, backtest |
| Frontend | `frontend/` | Dashboard, picks, stock detail, backtest |
| Rule SSOT | `rule_database/` | MVP 26 rules fully documented |
| Ops DB | Alembic scaffold | Picks JSON primary; PostgreSQL deferred v2.0 |

`mvp_mode: true` (default) — Trend + MA + Volume only. Full 16-domain mode: `mvp_mode: false` (v1.3).

---

# 1. 목적 (Purpose)

본 문서는 TASS의 전체 시스템 구조를 정의한다.

이 문서는 프로젝트의 모든 개발자가 반드시 따라야 하는 시스템 설계 기준이며, Python, Backend, Frontend, Database, AI 개발은 모두 본 문서를 기준으로 한다.

TASS는 기능 중심이 아니라 **Engine 중심**으로 설계한다.

---

# 2. 시스템 철학

TASS는 하나의 프로그램이 아니다.

TASS는 여러 개의 독립적인 Engine이 연결되어 동작하는 플랫폼이다.

각 Engine은 하나의 역할만 수행한다.

Engine 간 직접 계산을 하지 않는다.

모든 Engine은 명확한 입력(Input)과 출력(Output)을 가진다.

---

# 3. 전체 구조

```
외부 데이터(API)

        │

        ▼

Data Adapter

        │

        ▼

Market Engine

        │

        ▼

Filter Engine

        │

        ▼

Indicator Engine

        │

        ▼

Rule Engine

        │

        ▼

Score Engine

        │

        ▼

Gate Engine

        │

        ▼

Confidence Engine

        │

        ▼

Recommendation Engine

        │

        ▼

Report Engine

        │

        ▼

REST API

        │

        ▼

Frontend(Web)
```

---

# 4. Engine 구성

## Engine 1 : Data Adapter

역할

외부 API 데이터를

TASS 표준 데이터로 변환한다.

입력

* KIS
* 키움
* Yahoo
* 기타 API

출력

TASS 표준 데이터

---

## Engine 2 : Market Engine

역할

시장 전체를 분석한다.

분석 대상

* KOSPI
* KOSDAQ
* 시장 방향
* 시장 강도
* 시장 리스크

출력

Market Status

예)

BULL

NEUTRAL

BEAR

---

## Engine 3 : Filter Engine

역할

2700개 종목을

후보 종목으로 줄인다.

필터

* 거래량
* 거래대금
* 유동성
* 기본 추세

출력

100~300개 후보 종목

---

## Engine 4 : Indicator Engine

역할

모든 기술적 지표 계산

예)

MA

MACD

RSI

ATR

OBV

Bollinger

VWAP

ADX

DMI

Relative Strength

출력

Indicator Dataset

---

## Engine 5 : Rule Engine

역할

Rule 실행

예)

TREND

MA

VOLUME

RSI

MACD

각 Rule 계산

출력

Rule Result

---

## Engine 6 : Score Engine

역할

Rule 결과를 점수로 변환

예)

Trend

180

MA

135

Volume

140

Momentum

120

출력

Total Score

---

## Engine 7 : Gate Engine

역할

필수 통과 여부 확인

예)

시장

FAIL

↓

추천 제외

출력

PASS

FAIL

---

## Engine 8 : Confidence Engine

역할

추천 신뢰도 계산

평가

* 지표 일치성
* 추세 일치성
* 거래량
* 다중 시간프레임

출력

0~100%

---

## Engine 9 : Recommendation Engine

역할

최종 추천 종목 생성

출력

TOP20

추천 종목

추천 순위

---

## Engine 10 : Report Engine

역할

사용자에게 보여줄 분석 결과 생성

출력

* 총점
* 신뢰도
* 추천 이유
* 감점 이유
* 손절
* 익절
* 보유기간

---

# 5. Backend 구조

Backend는

FastAPI 기반으로 개발한다.

역할

* API 제공
* Engine 실행
* Database 연결
* AI 연동

Backend는

UI를 담당하지 않는다.

---

# 6. Frontend 구조

Frontend는

Next.js 기반으로 개발한다.

역할

* 추천 종목 표시
* 상세 분석 표시
* 사용자 설정
* 검색
* 대시보드

Frontend는

계산하지 않는다.

---

# 7. Database

역할

저장

* 주가 데이터
* 지표 데이터
* Rule 결과
* 점수
* 추천 기록
* 백테스트 결과

Database는

계산하지 않는다.

---

# 8. API

REST API 기반

예시

GET /recommendations

GET /stocks/{code}

GET /reports/{code}

GET /scores/{code}

GET /backtest

API는

계산하지 않는다.

Engine 결과만 전달한다.

---

# 9. Engine 원칙

모든 Engine은

다음 원칙을 따른다.

* 하나의 책임만 가진다.
* 독립적으로 테스트 가능해야 한다.
* 독립적으로 수정 가능해야 한다.
* 다른 Engine 내부를 직접 호출하지 않는다.
* 표준 데이터만 사용한다.

---

# 10. 개발 원칙

새로운 기능은

기존 Engine을 수정하는 것이 아니라

새로운 Engine 또는 Module로 추가한다.

기존 Engine을 최대한 변경하지 않는다.

---

# 11. AI 개발 원칙

Cursor

Claude Code

Codex

GitHub Copilot

모든 AI는

Engine 단위로 개발한다.

프로젝트 전체를 임의로 수정하지 않는다.

---

# 12. 테스트 전략

각 Engine은

독립적으로 테스트한다.

예)

Indicator Engine Test

Rule Engine Test

Score Engine Test

Gate Engine Test

Confidence Engine Test

Recommendation Engine Test

---

# 13. 향후 확장

향후 추가 예정

Learning Engine

Optimization Engine

Portfolio Engine

Risk Simulation Engine

Alert Engine

Notification Engine

Mobile API

AI Chat Engine

기존 Engine 구조는 변경하지 않는다.

---

# 14. 최종 사용자 흐름

1. 사용자가 웹사이트 접속

2. Today's Picks 확인

3. 추천 종목 클릭

4. 점수 확인

5. 추천 이유 확인

6. 손절·익절 확인

7. 매수 여부 결정

사용자는 차트를 분석하지 않는다.

TASS가 분석을 대신 수행한다.

---

# 15. 핵심 설계 원칙

TASS는 하나의 거대한 프로그램이 아니다.

TASS는 독립적인 Engine들이 협력하여 동작하는 투자 플랫폼이다.

모든 Engine은 독립적이어야 하며,

모든 결과는 재현 가능해야 하고,

모든 계산은 백테스트로 검증 가능해야 한다.

---

# 16. 다음 문서

**TASS-004 : Rule Framework**

다음 문서에서는 TASS의 모든 Rule이 따라야 하는 공통 구조를 정의한다.

아직 다우 이론이나 그랜빌 규칙을 만들지 않는다.

먼저 "Rule를 어떻게 작성할 것인가"라는 규격(Specification)을 만든다.

Rule Framework가 완성된 후에야 TREND-001, MA-001 등의 실제 Rule을 작성한다.
