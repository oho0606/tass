# TASS-032 : Application Layer

**Version:** v1.0

**Status:** Frozen

---

# Purpose

Application Layer는 Engine과 Presentation(API, CLI) 사이의 **조율 계층**이다.

Business Logic은 Application Layer에 존재하지 않는다.

Application Layer는 다음만 수행한다.

- 설정 로드
- Engine 파이프라인 호출
- 결과 직렬화 및 저장
- 로깅

---

# Architecture

```
CLI / API (future)
  ↓
Application Service
  ↓
Engine Layer (Trend, Gate, Scoring, …)
  ↓
Data Adapter
```

---

# Services

| Service | Responsibility |
|---------|----------------|
| `RecommendationService` | Today's Picks 생성·저장 |
| `BacktestService` | Rule 백테스트 실행·리포트 저장 |

---

# Module Structure

| Module | Contents |
|--------|----------|
| `recommendation_service.py` | `RecommendationService` |
| `backtest_service.py` | `BacktestService` |
| `settings.py` | `PipelineSettings`, `load_pipeline_settings()` |
| `serializers.py` | JSON/CLI 직렬화 |
| `types.py` | `DailyPicksResult`, `BacktestServiceResult` |

---

# RecommendationService

### Methods

| Method | Description |
|--------|-------------|
| `generate_daily_picks()` | Universe → Engine pipeline → picks |
| `save_daily_picks()` | JSON 저장 |
| `run_daily_picks()` | generate + save |

### Testing Hook

`ohlcv_overrides: dict[str, DataFrame]` — 네트워크 없이 테스트 가능.

---

# BacktestService

`BacktestEngine`을 래핑하여 리포트 I/O를 Application Layer에서 처리한다.

---

# CLI Integration

```bash
python main.py picks --universe config/universe_sample.csv
python main.py backtest
```

내부적으로 Application Service를 호출한다.

---

# Principles

1. Application Service는 Rule/Score를 계산하지 않는다.
2. Engine Layer를 수정하지 않는다.
3. 모든 설정은 `config/`에서 로드한다.
4. API Layer는 Application Service만 호출한다 (향후).

---

# Implementation Status

| # | Layer | Status |
|---|-------|--------|
| 10 | Backtest | ✅ v1.0 |
| — | Application | ✅ v1.0 |
| 11 | REST API | ⬜ Last |
| 12 | Frontend | ⬜ Planned |

---

# References

- TASS-030 Python Implementation Specification
- TASS-031 Backtest Engine
