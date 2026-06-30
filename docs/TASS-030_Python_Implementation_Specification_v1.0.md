# TASS-030 : Python Implementation Specification

**Version:** v1.0

**Status:** Frozen

**Author:** TASS Project

---

# 1. 목적 (Purpose)

본 문서는 TASS의 공식 Python 구현 표준이다.

모든 Python 코드는 본 문서를 기준으로 개발한다.

구현은 아래 순서를 반드시 따른다.

```text
Project Constitution
↓
Architecture
↓
Rule
↓
Composite Rule
↓
Engine
↓
Score
↓
Recommendation
```

설계와 다른 구현은 허용하지 않는다.

---

# 2. Python Version

| 항목 | 값 |
|------|-----|
| Target | Python 3.13+ |
| Minimum (MVP) | Python 3.11+ |

MVP 단계에서는 3.11+를 허용하며, 프로덕션 배포 전 3.13+로 승격한다.

---

# 3. Technology Stack

## 3.1 Core (현재 사용)

| Package | 용도 |
|---------|------|
| Pandas | OHLCV DataFrame |
| NumPy | 수치 계산 |
| Pydantic | 설정·DTO 검증 |
| PyYAML | 설정 파일 |
| PyTest | 테스트 |

## 3.2 Planned (단계별 도입)

| Package | Phase | 용도 |
|---------|-------|------|
| FastAPI + Uvicorn | API | REST API |
| SQLAlchemy + PostgreSQL | Data | 영구 저장 |
| Redis | Cache | 세션·캐시 |
| Polars | Performance | 대량 분석 (선택) |
| TA-Lib | Indicator | 기술 지표 |
| SciPy | Statistics | 확률·보정 |
| Loguru | Logging | 구조화 로그 |
| APScheduler | Jobs | 일일 배치 |
| Black, Ruff, isort, mypy | Quality | 코드 품질 |

`pyproject.toml`의 optional dependency group으로 관리한다.

---

# 4. Coding Principles

1. 모든 코드는 Type Hint를 사용한다.
2. 모든 Public 함수·클래스는 Docstring을 가진다.
3. 모든 함수는 Single Responsibility Principle을 따른다.
4. 모든 Module은 독립적으로 테스트 가능해야 한다.
5. Magic Number를 금지한다. (`config/`에서 관리)
6. Global Variable을 금지한다.
7. Business Logic은 UI에 존재하면 안 된다.
8. Business Logic은 API Layer에 존재하면 안 된다.
9. Business Logic은 Engine Layer에서만 수행한다.
10. 모든 코드는 Black Formatter를 따른다.

---

# 5. Directory Structure

TASS 프로젝트 루트 구조. `engine/`이 표준 `src/`에 해당한다.

```text
TASS/
├── engine/              # Python 구현 루트 (≡ src/)
│   ├── core/            # 타입, 예외, 로깅, Rule 베이스
│   ├── indicators/      # Indicator
│   ├── data/            # Data Adapter, Universe
│   ├── rules/           # Atomic Rule, Composite Rule
│   ├── domains/         # Domain Engine
│   ├── gate/            # Gate Engine
│   ├── scoring/         # Scoring Engine
│   ├── probability/     # Probability Engine
│   ├── confidence/      # Confidence Engine
│   ├── risk/            # Risk Engine
│   ├── recommendation/  # Recommendation Engine
│   ├── backtest/        # Backtest Engine (planned)
│   └── application/     # Application Service (planned)
├── api/                 # REST API Layer (planned)
├── tests/               # Unit, Integration, Regression
├── docs/                # 설계 문서 (TASS-001~030)
├── config/              # YAML 설정 + Pydantic Settings
├── scripts/             # CLI 도구
├── logs/                # 런타임 로그
├── database/            # DB 마이그레이션·스키마 (planned)
├── rule_database/       # Rule 메타데이터 DB
├── specs/               # Machine-readable Rule specs
├── agents/              # AI 역할 정의
├── skills/              # AI 절차 표준
├── main.py              # 애플리케이션 진입점
├── pyproject.toml
├── requirements.txt
├── .env
└── README.md
```

---

# 6. Layer Structure

```text
core
↓
indicators
↓
rules (atomic)
↓
rules (composite)
↓
domains (engines)
↓
gate
↓
scoring
↓
probability
↓
confidence
↓
risk
↓
recommendation
↓
backtest
↓
application
↓
api
↓
web (frontend, 별도 repo 가능)
```

---

# 7. Rule Standard

## Atomic Rule

- One Class · One File

```text
MA001 → price_above_sma20.py → PriceAboveSMA20Rule
```

## Composite Rule

- One Class · One File

```text
CTR001 → trend_quality.py → TrendQualityComposite
```

## Engine

- One Class · One File

```text
trend_engine.py → TrendEngine
```

---

# 8. Class Naming

| Layer | Pattern | Example |
|-------|---------|---------|
| Rule | `{Name}Rule` | `TR0001HigherHighRule` |
| Composite | `{Name}Composite` | `TrendQualityComposite` |
| Engine | `{Name}Engine` | `TrendEngine`, `RiskEngine` |
| Service | `{Name}Service` | `BacktestService` |
| Repository | `{Name}Repository` | `MarketRepository` |

---

# 9. Function Naming

snake_case: `calculate_score()`, `evaluate()`, `analyze()`, `recommend()`, `validate()`, `backtest()`, `load_data()`, `save_result()`

---

# 10. Return Types

| Layer | Return Type |
|-------|-------------|
| Atomic Rule | `bool` (verdict via `RuleResult`) |
| Composite Rule | `PASS` / `PARTIAL` / `FAIL` / `UNKNOWN` |
| Domain Engine | `float` |
| Scoring Engine | `float` |
| Probability | `float` |
| Confidence | `int` |
| Risk | `int` |
| Recommendation | `RecommendationResult` |

타입 정의: `engine/core/types.py`

---

# 11. Exception Rule

모든 Exception은 `engine/core/exceptions.py`의 Custom Exception을 사용한다.

| Exception | 용도 |
|-----------|------|
| `TassError` | 기본 예외 |
| `RuleException` | Rule 평가 실패 |
| `EngineException` | Engine 실행 실패 |
| `DataException` | 데이터 로드·검증 실패 |
| `BacktestException` | 백테스트 실패 |
| `RecommendationException` | 추천 생성 실패 |

---

# 12. Logging

`engine/core/logging.py` — Loguru 기반.

| Level | 용도 |
|-------|------|
| DEBUG | Rule/Engine 중간값 |
| INFO | 파이프라인 진행 |
| WARNING | Gate Fail, 데이터 부족 |
| ERROR | 예외·복구 불가 |
| CRITICAL | 시스템 중단 |

환경 변수 `LOG_LEVEL`, `logs/` 디렉터리 사용.

---

# 13. Configuration

| 위치 | 용도 |
|------|------|
| `config/*.yaml` | Engine·Rule 파라미터 |
| `config/app_settings.py` | `.env` → Pydantic Settings |
| `.env` | 시크릿·인프라 연결 |

하드코딩 금지.

### Environment Variables

```text
DATABASE_URL
REDIS_URL
API_KEY
JWT_SECRET
LOG_LEVEL
TIMEZONE
```

---

# 14. Dependency Rule

```text
Indicator → Atomic Rule → Composite Rule → Engine
→ Score → Probability → Confidence → Risk
→ Recommendation → Backtest → API → Frontend
```

- 역참조 금지
- 순환참조 금지
- Rule는 Engine을 참조하지 않는다
- Engine은 Rule를 수정하지 않는다

---

# 15. Testing

| 유형 | 대상 | Coverage |
|------|------|----------|
| Unit Test | 모든 Class | 90%+ |
| Integration Test | 모든 Engine | 필수 |
| Regression Test | Rule 변경 시 | 자동 |

테스트 위치: `tests/unit/`, `tests/integration/`, `tests/regression/`

---

# 16. Performance Target

| Layer | Target |
|-------|--------|
| Atomic Rule | < 0.5 ms |
| Composite Rule | < 2 ms |
| Engine | < 5 ms |
| Recommendation | < 30 ms |
| 3000 종목 분석 | < 5 sec |

---

# 17. Code Quality

| Tool | Config |
|------|--------|
| Black | `pyproject.toml` |
| Ruff | `pyproject.toml` |
| isort | `pyproject.toml` |
| mypy | `pyproject.toml` |
| pytest | `pyproject.toml` |
| pre-commit | `.pre-commit-config.yaml` |
| GitHub Actions | `.github/workflows/ci.yml` |

---

# 18. Git Strategy

```text
main → release → develop
feature/*, bugfix/*, hotfix/*
```

### Commit Convention

`feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `style`, `build`, `ci`

### Release Policy

Semantic Versioning: Major · Minor · Patch

---

# 19. Implementation Order

| # | Layer | TASS Status |
|---|-------|-------------|
| 1 | Indicator | ✅ Partial |
| 2 | Atomic Rule | ✅ **18 categories × 60 rules = 1,080** (spec-driven runtime) |
| 3 | Composite Rule | ✅ Partial (CTR) |
| 4 | Domain Engine | ✅ Trend, Moving Average |
| 5 | Scoring | ✅ v1.0 |
| 6 | Probability | ✅ v1.0 |
| 7 | Confidence | ✅ v1.0 |
| 8 | Risk | ✅ v1.0 |
| 9 | Recommendation | ✅ v1.0 |
| 10 | Backtest | ✅ v1.0 |
| — | Application | ✅ v1.0 |
| 11 | REST API | ⬜ Last |
| 12 | Frontend | ⬜ Planned |

---

# 20. Build Pipeline

```text
Git Push → Lint → Unit Test → Integration Test
→ Regression Test → Build → Docker → Deploy
```

---

# 21. Summary

| 항목 | 값 |
|------|-----|
| Language | Python 3.11+ (target 3.13+) |
| Architecture | Clean / Layered |
| Implementation Root | `engine/` |
| Formatter | Black |
| Type Checking | mypy |
| Deployment | Docker (planned) |
| Status | Frozen v1.0 |

본 문서는 TASS 프로젝트의 공식 Python 구현 표준이며, 모든 구현은 본 문서를 기준으로 개발한다.
